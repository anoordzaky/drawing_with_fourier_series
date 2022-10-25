from presentation import *
import numpy as np
import argparse

def run(source, order, target, fps, space):

    print('Processing Image...')
    time_table, x_table, y_table = create_close_loop(source)
    tlr = 50
    xmin, xmax = min(x_table) + tlr, max(x_table) + tlr
    ymin, ymax = min(y_table) + tlr, max(y_table) + tlr

    print('Calculating coefficients...')
    coef = coef_list(time_table, x_table, y_table, order)
    space = np.linspace(0, tau, space)
    x_DFT = [DFT(t, coef, order)[0] for t in space]
    y_DFT = [DFT(t, coef, order)[1] for t in space]

    print('Visualizing....')
    anim = visualize(x_DFT, y_DFT, coef, order, space, [xmin, xmax, ymin, ymax])
    writer = animation.writers['ffmpeg']
    writer = writer(fps=fps)

    print('Exporting...')
    return anim.save(target, writer=writer)

def parse_opt():
    parser = argparse.ArgumentParser(description = 'Optional parameters')
    parser.add_argument('--source', type=str, default='image/mandelbrot.jpg', help='image source path')
    parser.add_argument('--order', type=int, default=100, help='n order of the fourier series')
    parser.add_argument('--target', type=str, default='mb.mp4', help='video target path in .mp4 format')
    parser.add_argument('--fps', type=int, default=60, help='target fps of the video')
    parser.add_argument('--space', type=int, default=600, help='length of the x axis of the fourier series (space/fps=video length(s))')
    opt = parser.parse_args()
    return opt
if __name__ == '__main__':

    opt = parse_opt()
    print(opt)
    run(**vars(opt))


