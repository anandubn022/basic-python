from PIL import Image, ImageFilter
before = Image.open("images/link.png")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("images/blur_output.png")
