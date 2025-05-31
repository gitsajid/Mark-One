# FACE-RECOGNITION 
import setuptools
import cv2 as cv
import face_recognition
import os, sys
import numpy, math
from colorama import Fore

def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_value = (1.0 - face_distance) / (range * 2.0)
    
    if face_distance > face_match_threshold:
        return round(linear_value * 100, 2)
    
    else:
        value = (linear_value + ((1.0 - linear_value) * math.pow((linear_value - 0.5) * 2, 0.2))) * 100
        return round(value, 2)
    
class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = [] # FACES AT CURRENT FRAME
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True 
    access = False
    
    current_dir = os.getcwd()
    face_file_path = rf"{current_dir}\Authentications\FaceRecRef\admin"
    
    def __init__(self):
        self.encode_faces()
    
    def encode_faces(self):
        print(Fore.GREEN + "Encoding...")
        for image in os.listdir(self.face_file_path):
            image_path = os.path.join(self.face_file_path, image)
            face_image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(face_image)
            if encoding:
                face_encoding = encoding[0]
            else:
                print(Fore.RED + f"No face found in {image}")
                continue
            
            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image)
        
        print(Fore.YELLOW + "---Encoding successful---")
        # print(self.known_face_names)
        
    def run_recognition(self):
        print(Fore.YELLOW + "Scanning...")
        
        screen_capture = cv.VideoCapture(0)
        
        if not screen_capture.isOpened():
            sys.exit(Fore.RED + "Video source not found...")
            
        while True:
            ret, frame = screen_capture.read()
            
            if self.process_current_frame:
                small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = cv.cvtColor(small_frame, cv.COLOR_BGR2RGB)
                
                #FIND ALL FACES AT THE CURRENT FRAME
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
                
                self.face_names = []
                for live_face_encoding in self.face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_encodings, live_face_encoding)
                    name = "UNKNOWN"
                    confidence = "UNKNOWN"
                    
                    face_distance_val = face_recognition.face_distance(self.known_face_encodings, live_face_encoding)
                    best_match_idx = numpy.argmin(face_distance_val)
                    
                    if matches[best_match_idx]:
                        name = self.known_face_names[best_match_idx]
                        confidence = face_confidence(face_distance_val[best_match_idx])
                        
                        print(Fore.GREEN + "Authenticating...")
                        
                        # ACCESS CAN BE CONTROLLED FROM HERE
                        count = 0
                        
                        while count < 4:
                            if confidence > 95:
                                print(Fore.GREEN + "Access granted...")
                                self.access = True
                                return self.access
                            
                            else:
                                print(Fore.RED + "Acsess denied...")
                                count += 1
                                
                            if count == 4:
                                print(Fore.RED + "---Too many failed attempt---")
                                exit()
                        
                    self.face_names.append(f"{name} {str(confidence) + "%"}")
            
                   
            self.process_current_frame = not self.process_current_frame
            
            # DISPLAY
            # for(top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            #         top *= 4
            #         right *= 4
            #         bottom *= 4
            #         left *= 4
                    
            #         cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            #         cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), -1)
            #         cv.putText(frame, name, (left + 6, bottom - 6), cv.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)
                    
            # cv.imshow("Face Recognition", frame)
            
            # if cv.waitKey(1) == ord("q"):
            #     break
            
        # screen_capture.release()
        # cv.destroyAllWindows()
        
        
        
if __name__ == "__main__":
    a = FaceRecognition().run_recognition()
    print(a)
        
            
        
