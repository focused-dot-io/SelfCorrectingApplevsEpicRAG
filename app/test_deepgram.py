import os
from dotenv import load_dotenv
from langsmith import traceable
from deepgram import DeepgramClient, PrerecordedOptions


# The API key we created in step 3
# DEEPGRAM_API_KEY = 'YOUR_SECRET'

# Hosted sample file
AUDIO_URL = {
    'url': 'https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav'
}

@traceable
def main():
    load_dotenv()
    deepgram = DeepgramClient(os.getenv("DEEPGRAM_API_KEY"))

    options = PrerecordedOptions(
        smart_format=True, model="nova-2", language="en-US", utterances=True
    )

    response = deepgram.listen.prerecorded.v('1').transcribe_url(AUDIO_URL, options)
    print(response)


if __name__ == '__main__':
    main()
