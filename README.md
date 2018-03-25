## oekakiLogic
Generate the 'oekaki-logic' problem (Japanese image puzzle).

## Usage

``` sh
$ python3 gen_oekaki.py --img ./image/nobunaga.gif --game_w 32 --game_h 32 --black_threshold 100
$ python3 gen_oekaki.py --img ./image/nobunaga.gif
```

## Example

- 32x32 sample, from [PixelGaro](https://hpgpixer.jp/)
![original_image](./image/nobunaga.gif, "original image")
![output_image](./image/nobunaga_enlarge.gif, "problem image")

- 200x200 sample, from [rakugaki.com](http://rakugakiicon.com/)
![original_image](/image/doctor.png, "original image")
![output_image](/image/doctor_enlarge.gif, "problem image")
