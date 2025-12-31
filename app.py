import speech_recognition as sr
from gtts import gTTS
import os
import pygame
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client=OpenAI(api_key=os.getenv("API_KEY"))

chat_history=[
    {"role":"system","content":"""
    【設定】
    あなたは【患者の佐々木】という特定のキャラクターを演じる専用AIです。
    以下の「絶対厳守ルール」に従ってください。
    ■絶対厳守ルール
    1. あなたは「病院に電話をかけた患者」です。
    2. ユーザーは「病院の受付」です。
    3. ユーザーに対して「あなたの役は〜です」といった指示や解説、メタ的な発言は【一切禁止】です。
    4. 受付（ユーザー）のような丁寧な案内（「予約を承りました」等）をすることも【一切禁止】です。
    5. あなたは「熱があって困っている」という自分の状況だけを話してください。
    6. 予約が取れたら「ありがとうございました」と言って電話を切ってください
   【設定】
    38.5度の熱と喉の痛みがあり、非常に体調が悪いです。今日中に受診したいです。
    【評価フェーズへの移行条件】
    ユーザーが「失礼します」と言ったり、予約が完了して電話を切る流れになったら、患者役を終了し、「評価モード」に入ってください。
    【評価項目（各20点 / 合計100点）】
    1.挨拶と名乗り: 病院名を正しく伝え、丁寧な挨拶ができたか
    2.傾聴スキル: 患者の症状を正確に聞き出し、共感を示したか
    3.正確性: 予約日時や持ち物（保険証など）を漏れなく伝えたか
    4.言葉遣い: 適切な敬語（クッション言葉）が使えていたか
    5.安心感: 相手を不安にさせないトーンだったか
    """}
]

def get_ai_response(user_text):
    chat_history.append({"role":"user","content":user_text})
    completion=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history,
        temperature=0.7
    )
    ai_response= completion.choices[0].message.content
    chat_history.append({"role":"assistant","content":ai_response})
    return ai_response

def speak(text):
    print(f"\n患者:{text}")
    file_name="response.mp3"
    tts=gTTS(text=text, lang="ja")
    tts.save(file_name)

    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()
    pygame.mixer.quit()

    if os.path.exists(file_name):
        os.remove(file_name)

def recognize_audio():
    recognizer=sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("受付として対応してください。(Ctrl+Cで終了)")
            audio=recognizer.listen(source)
        try:
            text=recognizer.recognize_google(audio, language="ja-JP")
            print(f"あなた:{text}")
            if any(word in text for word in ["失礼します","失礼いたします", "お電話ありがとうございました"]):
                print("\n評価を開始します")
                evaluation_request = "ロープレを終了します。これまでの会話履歴を分析し、「病院の受付役」を担当した【ユーザー】の対応を、患者の視点から5つの項目で厳しく採点してください。AIであるあなた自身の評価は不要です。"
                response=get_ai_response(evaluation_request)
                speak(response)
                break
            response=get_ai_response(text)
            speak(response)
        except sr.UnknownValueError:
            print("音声を理解できませんでした。")
        except sr.RequestError:
            print("サーバーに接続できませんでした。")

if __name__ == "__main__":
    recognize_audio()