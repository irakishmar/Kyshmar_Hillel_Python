import re

# # import file (please comment out the next line text and check additional task)
# document = open('text.txt', 'r')
# text = str(document.readlines())

# text from string
text = "The Hubble.Space.Telescope (often referred to as HST or Hubble) is a space telescope that was launched into low Earth orbit in 1990 and remains in operation.... It was not the first space telescope, but it is one of the largest and most versatile, renowned both as a vital research tool and as a public relations boon for astronomy. The Hubble telescope is named after astronomer Edwin Hubble and is one of NASA's Great Observatories..... The Space Telescope Science Institute (STScI) selects Hubble's targets and processes the resulting data, while the Goddard Space Flight Center (GSFC) controls the spacecraft.A commission headed by Lew Allen, director of the Jet Propulsion Laboratory, was established to determine how the error could have arisen. The Allen Commission found that a reflective null corrector, a testing device used to achieve a properly shaped non-spherical mirror, had been incorrectly assembled—one lens was out of position by 1.3 mm (0.051 in)."
sentence_list = re.split(r'\.{3,}\s|\.\s', text)
for element in sentence_list:
    new_elements = re.findall(r'\.\s|\.[A-Z]\s', element)
    if len(new_elements) > 0:
        item = re.split(r'\.', element)
        for part in item:
            print(part)
    else:
        print(element)
