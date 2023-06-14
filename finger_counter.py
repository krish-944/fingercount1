import cv2
import time
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

new_frame_time = 0
prev_frame_time = 0

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
  min_detection_confidence=0.5,
  min_tracking_confidence=0.5,
  max_num_hands=2) as hands :

  while cap.isOpened():

    success,image = cap.read()
    if not success :
      print("Skipping empty frame !")
      continue
    
    image = cv2.flip(image,1)

    results = hands.process(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

    hand = str(results.multi_handedness)

    if 'Right' in hand :
      whathand = 'Hand : Right'
    elif 'Left' in hand :
      whathand = 'Hand : Left'
    else :
      whathand = 'Hand : -'
    
    image.flags.writeable = True
    imageHeight, imageWidth, _ = image.shape
    
    gesture = 'Gesture : -'    

    if results.multi_hand_landmarks :
      for hand_landmarks in results.multi_hand_landmarks :
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(16,31,235), thickness=4, circle_radius=3,), # Land Mark
        mp_drawing.DrawingSpec(color=(52,235,155), thickness=2)) # Land Connections
        
        
        normalizedLandmark = hand_landmarks.landmark[4]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Thumb_Tip_x = pixelCoordinatesLandmark[0]           
        Thumb_Tip_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[6]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Index_Pip_x = pixelCoordinatesLandmark[0]           
        Index_Pip_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[10]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Middle_Pip_x = pixelCoordinatesLandmark[0]           
        Middle_Pip_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[14]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Ring_Pip_x = pixelCoordinatesLandmark[0]           
        Ring_Pip_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[18]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Pinky_Pip_x = pixelCoordinatesLandmark[0]           
        Pinky_Pip_y = pixelCoordinatesLandmark[1]
        #--------------------------------------------------
        normalizedLandmark = hand_landmarks.landmark[5]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Index_Mcp_x = pixelCoordinatesLandmark[0]           
        Index_Mcp_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[9]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Middle_Mcp_x = pixelCoordinatesLandmark[0]           
        Middle_Mcp_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[13]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Ring_Mcp_x = pixelCoordinatesLandmark[0]           
        Ring_Mcp_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[17]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Pinky_Mcp_x = pixelCoordinatesLandmark[0]           
        Pinky_Mcp_y = pixelCoordinatesLandmark[1]

        #------------------------------------
        normalizedLandmark = hand_landmarks.landmark[3]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Thumb_Ip_x = pixelCoordinatesLandmark[0]           
        Thumb_Ip_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[8]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Index_Tip_x = pixelCoordinatesLandmark[0]           
        Index_Tip_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[12]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Middle_Tip_x = pixelCoordinatesLandmark[0]           
        Middle_Tip_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[16]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Ring_Tip_x = pixelCoordinatesLandmark[0]           
        Ring_Tip_y = pixelCoordinatesLandmark[1]

        normalizedLandmark = hand_landmarks.landmark[20]# Point No.
        pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
        Pinky_Tip_x = pixelCoordinatesLandmark[0]           
        Pinky_Tip_y = pixelCoordinatesLandmark[1]

        thmb_indx_diff = Thumb_Ip_x-Index_Mcp_x

        if Index_Pip_y < Middle_Tip_y and Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y :
            if Index_Tip_y < Middle_Pip_y and Index_Tip_y < Ring_Pip_y and Index_Tip_y < Pinky_Pip_y :
                gesture = 'Gesture : One'  

        if Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y :
            if Middle_Tip_y < Ring_Pip_y and Middle_Tip_y < Pinky_Pip_y :
                gesture = 'Gesture : Two'  

        if Index_Pip_y < Pinky_Tip_y and Middle_Pip_y < Pinky_Tip_y and Ring_Pip_y < Pinky_Tip_y  :
            if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y :
                if Index_Tip_y < Thumb_Tip_y and Middle_Tip_y < Thumb_Tip_y and Ring_Tip_y < Thumb_Tip_y :
                    gesture = 'Gesture : Three'   

        if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y  :
            if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y :
                gesture = 'Gesture : Four' 

        if thmb_indx_diff < -15 :
            if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y :
                gesture = 'Gesture : Five'
        
    
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps2text = 'FPS : '+str(int(fps))


    cv2.rectangle(image,(5,5),(320,110),(0,170,240),-1)
    cv2.putText(image,gesture,(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)     
    cv2.putText(image,fps2text,(20,90),cv2.FONT_HERSHEY_COMPLEX,1,(3,3,138),2)
    cv2.imshow('Hand Detection',image)     

    if cv2.waitKey(5) & 0xFF == 27 :
      break

cap.release()
