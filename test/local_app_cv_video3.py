# pip install google-generativeai
# python -m pip install --upgrade pip

import os
import google.generativeai as genai
from PIL import Image
import cv2

mygoogleapikey = 'AIzaSyDmbIadSL9Ot8CCH1ilPlOdBgO41-MXr-Q'   # 個人的api金鑰
genai.configure(api_key= mygoogleapikey)
model = genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

def analyze_video(video_path, input_prompt):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    results = []

    cv2.namedWindow('Video Analysis')  # 創建一個名為 'Video Analysis' 的視窗

    for i in range(frame_count):
        ret, frame = cap.read()
        # responseOnScreen = ''
        if not ret:
            break

        if i % (fps) == 0:
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            response = get_gemini_response(input_prompt, image)
            results.append({"frame_number": i, "action": response})
            # print(response)
            print(results[-1]['action'])
            # 在畫面左上角顯示回應狀態
            # cv2.putText(frame, response, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)        
        cv2.putText(frame, results[-1]['action'], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Video Analysis', frame)  # 顯示畫面
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按下 'q' 鍵退出
            break

    cap.release()
    cv2.destroyAllWindows()  # 關閉所有視窗
    return results

# 範例用法
# video_path = 'video/pushup3.mp4'  # 替換成您的影片路徑
video_path = 'video/collect_workout3.mp4'

input_prompt = '請問畫面中人物在做什麼 , 請最簡單回答 如: Squat, Jump, Pullup, Pushup, Run, Walk, Rest'
results = analyze_video(video_path, input_prompt)
# print(results)
import json
with open('video_analysis_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("影片分析結果已儲存至 video_analysis_results.json")


