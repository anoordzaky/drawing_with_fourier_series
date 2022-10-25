# Drawing with Fourier Series
Drawing image contours using Fourier Series.

## Cloning and accessing the repo
To clone and access the file:
```
git clone https://github.com/anoordzaky/drawing_with_fourier_series
cd drawing_with_fourier_series
```

## Requirements
To install required modules:
```
pip install -r requirements.txt
```
<p>Also need to install FFMPEG from here https://ffmpeg.org/</p>
Useful article on installing FFMPEG: https://suryadayn.medium.com/error-requested-moviewriter-ffmpeg-not-available-easy-fix-9d1890a487d3

## Running the script

```
python run.py	--source image/mandelbrot.jpg #source image path
		--order 100 #n order of the fourier series
		--target mb.mp4 #target directory to save the file in .mp4 format
		--fps 60 #num of fps of the video
		--space 600 #sum of the increments of t axis, affects video length (length = space/fps)
```

## Credit

Uses functions from WiraDKP's github: https://github.com/WiraDKP/Discrete_Fourier_Transform_Epicycle
