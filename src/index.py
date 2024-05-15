from services.text_splicer import text_processor
from services.pdf_sticher import PdfMaker

if __name__ == "__main__":
    information = """1 Arid Mesa (ZNE) 9
1 Badlands (30A) 273
1 Bayou (3ED) 283
1 Bloodstained Mire (KTK) 230
1 Command Tower (ELD) 333
1 Flooded Strand (KTK) 233
1 Ketria Triome (IKO) 250
1 Marsh Flats (ZEN) 219
1 Misty Rainforest (ZEN) 220
1 Plains (PIP) 317
1 Plateau (SUM) 284
1 Polluted Delta (KTK) 239
1 Raugrin Triome (IKO) 251
1 Savannah (SUM) 285
1 Scalding Tarn (ZEN) 223
1 Scrubland (SUM) 286
1 Taiga (PRM) 43618
1 Tropical Island (SUM) 288"""
    oneline = "1 Arid Mesa (ZNE) 9"
    onepage = """1 Arid Mesa (ZNE) 9
1 Badlands (30A) 273
1 Bayou (3ED) 283
1 Bloodstained Mire (KTK) 230
1 Command Tower (ELD) 333
1 Flooded Strand (KTK) 233
1 Ketria Triome (IKO) 250
1 Marsh Flats (ZEN) 219
1 Misty Rainforest (ZEN) 220"""

    data = text_processor(onepage)
    maker = PdfMaker(800, 401)
    maker.add_cards(data)
    maker.save('test.png')
