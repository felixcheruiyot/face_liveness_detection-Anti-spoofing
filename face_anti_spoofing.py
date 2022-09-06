import random 
import cv2
import imutils
import f_liveness_detection
import questions

# parameters 
COUNTER, TOTAL = 0,0
counter_ok_questions = 0
counter_ok_consecutives = 0
limit_consecutives = 3
limit_questions = 6
counter_try = 0
limit_try = 50 


def start(img):
    for i_questions in range(0,limit_questions):
        # genero aleatoriamente pregunta
        index_question = random.randint(0,5)
        question = questions.question_bank(index_question)

        for i_try in range(limit_try):
            # <----------------------- ingestar data 
            # ret, im = cam.read()
            im = imutils.resize(img, width=720)
            im = cv2.flip(im, 1)
            # <----------------------- ingestar data 
            TOTAL_0 = TOTAL
            out_model = f_liveness_detection.detect_liveness(im,COUNTER,TOTAL_0)
            TOTAL = out_model['total_blinks']
            COUNTER = out_model['count_blinks_consecutives']
            dif_blink = TOTAL-TOTAL_0
            if dif_blink > 0:
                blinks_up = 1
            else:
                blinks_up = 0

            challenge_res = questions.challenge_result(question, out_model,blinks_up)
            if challenge_res == "pass":
                counter_ok_consecutives += 1
                if counter_ok_consecutives == limit_consecutives:
                    counter_ok_questions += 1
                    counter_try = 0
                    counter_ok_consecutives = 0
                    break
                else:
                    continue

            elif challenge_res == "fail":
                counter_try += 1
            elif i_try == limit_try-1:
                break
                

        if counter_ok_questions ==  limit_questions:
            print("passed")
        elif i_try == limit_try-1:
            print("fail")
            break 

        else:
            continue
