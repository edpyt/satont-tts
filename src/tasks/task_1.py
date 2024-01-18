from tasks.yml_data import get_tts_yml_data


def main() -> None:
    silero_data: dict = get_tts_yml_data()

    for language in silero_data:
        print(f'Язык: {language}')

        print('Модели:')
        for model in silero_data[language]:
            print(' ' * 2, model)
        print()


if __name__ == '__main__':
    main()
