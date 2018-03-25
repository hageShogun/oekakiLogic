import numpy as np
from PIL import Image


def run_length(arr, target=0):
    suc_flg = False
    suc_num = 0
    ret = []
    for pix in arr:
        if pix == target:
            suc_num += 1
            if not suc_flg:
                suc_flg = True
        else:
            if suc_flg:
                ret.append(suc_num)
                suc_num = 0
                suc_flg = False
    if suc_flg:
        ret.append(suc_num)
    return ret


def gen_oekaki_logic(img, game_w, game_h, th=100):
    img = img.resize((game_w, game_h))
    img_bw = img.convert('L').point(lambda x: 0 if x<=th else 255)  # Black/White image
    img_arr = np.array(img_bw)  # Convert image to a numpy array

    # count row and column lines
    rows = [run_length(x) for x in img_arr]
    cols = [run_length(x) for x in img_arr.T]

    return (rows, cols)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', action='store', type=str)
    parser.add_argument('--game_w', action='store', type=int, default=32)
    parser.add_argument('--game_h', action='store', type=int, default=32)
    parser.add_argument('--black_threshold', action='store', type=int, default=100)    
    args = parser.parse_args()

    img = Image.open(args.img)
    rows, cols = gen_oekaki_logic(img, args.game_w, args.game_h)
    print('rows:',rows)
    print('cols:',cols)

    print('Final image:')
    img.resize((args.game_w, args.game_h)).convert('L').point(lambda x: 0 if x<=args.black_threshold else 255).resize((args.game_w*10,args.game_h*10)).show()
