from yml_data import get_tts_yml_data

silero_data: dict = get_tts_yml_data()
for language in silero_data:
    for _model in silero_data[language]:
        pass
