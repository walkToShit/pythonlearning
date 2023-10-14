import img2pdf
import os

photo_path1 = r'd://picture';


def from_photo_to_pdf(photo_path):
    '''photo_list = os.listdir(photo_path)'''
    photo_list = [os.path.join(photo_path, i) for i in os.listdir(photo_path)]; '''合成绝对路径'''
    j = 0;
    for i in photo_list:
        j = j+1;
        a4inpt = (img2pdf.mm_to_pt(720), img2pdf.mm_to_pt(1080))
        layout_fun = img2pdf.get_layout_fun(a4inpt)
        with open(photo_path+'\\result%d'%j+'.pdf', 'wb') as f:
            f.write(img2pdf.convert(i, layout_fun=layout_fun))


from_photo_to_pdf(photo_path1);
