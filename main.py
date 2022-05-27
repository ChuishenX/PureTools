def trans_any_audio_types(filepath, input_audio_type, output_audio_type):
    song = AudioSegment.from_file(filepath, input_audio_type)
    filename = filepath.split(".")[0]
    if os.getcwd() != "/static/":
        print(os.getcwd())
        os.chdir('./static/')
    song.export(f"{filename}.{output_audio_type}", format=f"{output_audio_type}")