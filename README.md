## 病院受付オペレーターのロールプレイ用AIシステム

コールセンターのロールプレイと、応対品質の評価ができます。

 - ロールプレイ画面
<img width="540" height="278" alt="ロールプレイ中の画像" src="https://github.com/user-attachments/assets/28c78858-5527-4742-afce-1cf9b4ac26a2" />


- 応対品質の評価画面
<img width="539" height="364" alt="応対品質評価中の画像" src="https://github.com/user-attachments/assets/b3bcecb4-f647-4742-95ee-a10eabfa49fc" />



### 1. 使用技術
 - 言語 : python
 - AI(LLM) : OPENAI API(GPT-4o-mini)
 - 音声認識 : SpeechRecognition(Google Speech Recgnition API)
 - 音声合成 : gTTS(Google Text-to-Speech)
 - オーディオ再生 : pygame
 - 環境変数管理 : python-dotenv

### 2. 起動方法
 - リポジトリをクローン
 - pip install -r requirements.txt
 - .envファイルを作成し、OpenAIのAPIキーを設定
 - python app.py
