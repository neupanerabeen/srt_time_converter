# utilities


I wanted to add srt file in VLC to view subtitles in a movie. But the time of dialogue in srt file didn't match the speech time in movie. This utility helps to change the time of dialogue in the srt filt to sync the time of speech in movies.  

python runner.py input_file destination_path lag
	input_file:SRT file to add/substract time
	destination_path: non-existant file path to write the processed src file
	lag: seconds to add/substract
