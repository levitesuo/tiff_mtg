# This is a plannin document for the v2

## Features

* [ ] Make all the requests in the program to use async requests.
* [ ] Don't scale the individual cards scale the page.
* [ ] Make it possible to use your own photos insted of the ones provided by the api.
    * [ ] First the pictuers must be the correct aspect ratio
    * [ ] Later make it possible for the user to scale up and down the custom photos, and move them.
* [ ] Confirmation ui for the cards before printing. (mtgprint)
* [ ] AI stuff?

## Code Structure

src/  
├─ services/  
│  ├─ upscale_servicse.py  
│  ├─ page_maker.py  
│  ├─ input_validition.py  
│  ├─ text_processor.py  
│  └─ ui_service.py  
├─ entitys/  
│  ├─ art.py  
│  ├─ card.py  
│  └─ page.py  
├─ repository (Holds all the api stuff)  
└─ ui  
