---
title: Long time code snippets
---

## PyTorch Associated

<pre> <code>
# Weight init: https://github.com/pytorch/pytorch/blob/master/torch/nn/init.py
from torch.nn import init
init.constant(self.conv1, 0)
</code></pre>


## Bash Commands

<pre> <code>
# FFMPEG
    ### Merge FLV videos
    LISTFN=$1; OUTVFN=$2
    for f in ./*.flv; do echo "file '$f'" >> ${LISTFN}; done
    ffmpeg -f concat -safe 0 -i ${LISTFN} -c copy ${OUTVFN}

# SED & TR & AWK & XARGS & SPLIT
    ### Replace characters
    echo "demo_string" | tr '_' '\t'
    
    ### Rename suffix ".suffixa" to ".suffixb"
    command = "find ./ -name \"*.suffixa\" | awk -F \".\" '{print $2}' | xargs -i -t mv ./{}.suffixa  ./{}.suffixb

    ### Captial to lower, lower to capital
    tr a-zA-Z A-Za-z < input.txt

    ### Split large scale file; -a sets the length of suffix, default is 2
    split -d -a 5 -l 70 ToSplitFile.txt SUFFIX 


# MISC
    ### Run Matlab
    matlab -nodisplay -nosplash -nodesktop -r \"run compute_mAP.m\"

    ### Concat several images to one image. - means vertical, + horizontal
    convert jpg_a.jpg jpg_b.jpg -/+append concat.jpg
    
    ### Modify login display info
    vim `/etc/motd` and `/etc/issue.net` and `/etc/issue`

    ### Mentohust mac with thunderbolt2 interface auth command
    sudo ~/localbin/mentohust_mac/mentohust -k; sudo ~/localbin/mentohust_mac/mentohust -uU201413322 -ps762352471 -nen6 -d2

    ### Convert excel file to csv
    brew install gnumeric; ssconvert fn.xlsx csvfn.csv

    ### Adjust the font/font-size for the TTY
    dpkg-reconfigure console-setup

    ### Pdf files to png images
    pdfimages -list $PDF_FN
    pdfimages $PDF_FN $IMG_FN
    find . -name "*.ppm" | while read line
    do
        convert $line $(echo $line | sed 's/\.ppm/\.png/')
    done
    # pdfjoin --papersize '{21.0cm,29.7cm}' *.png

    ### webp to png image
    dwebp FILENAME -o ${FILENAME//webp/png}



</code></pre>


# Tools

- [Generate html table - Bash](../codes/genhtmltable_bash.sh)
- [Replace half characters to full (Mac)- Python](../codes/enp2cnp.py)
- [Fanfou reader - Python](../codes/fanfou_reader.py)


