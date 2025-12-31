## 病院受付オペレーターのロールプレイ用AIシステム

コールセンターのロールプレイと、応対品質の評価ができます。

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