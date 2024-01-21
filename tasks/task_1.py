from yml_data import get_tts_yml_data

silero_data: dict = get_tts_yml_data()
for language in silero_data:
    print(f'Язык: {language}')
    print('Модели:')
    for model in silero_data[language]:
        print(' ' * 2, model)
    print()
