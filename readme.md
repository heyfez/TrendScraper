# TrendScraper - A simple Black Friday deal scraper for trendevice.com

## Disclamer

_EDUCATIONAL PURPOSE ONLY! We are **not affiliated** with any of the brands/companies mentioned. We are **not promoting** any of the brands/companies mentioned. We are **not advising** any of the brands/companies mentioned. Interacting with one of the brands/companies mentioned is **by your own choice**._

## Intro

I saw the Black Friday deal [HERE](https://www.ispazio.net/2035377/black-weeks-trendevice-iniziano-domani-3-11-non-perdere-liphone-11-a-1e-solo-1-disponibile): one iPhone 11 for one euro. Trendevice.com was releasing an Iphone 11 for one euro **at a random time**, **in a random variant**, between 12.00 and 13.00, \*\*one only!. So i made a really simple scraper to find the right variant to be purchased for 1 euro and to be notified in real time.

## Dependencies

- [coloredlogs](https://pypi.org/project/coloredlogs/)[^1] (optional)

## Description

The iPhone 11 for one euro was released at 12:46:28 and the scraper works great.
![Notification](/screen2.png)
I didn't code the AUTO-CHECKOUT part cause the website has got no anti-bot protection, and it has got a cart-holder system. So my manual checkout was really really fast using a trick: I signed-in and I saved all my personal infos in my account page. I made a pre-checkout with a random item available in stock and i stopped the checkout in the ApplePay confirmation page. Then i opened a new tab in the browser and i moved to initial cart page and removed the item in the cart and i closed it. Now i have got only the ApplePay confirmation page opened, ready for purchase, but with an empty cart.
Once the scraper found the product, it send me the link in the terminal. I opened in the browser, I added to the cart the iPhone 11 for one euro and then i moved to the ApplePay checkout page previously opened and I did the checkout. Using this checkout method I purchased the item in 1-2 seconds.
The order was made.
![Order](/screen1.png)
More commets in the code.

## WARNING

The order was made but the company didn't shipped the order to me. They canceled the order. **I don't know** if someone else was faster then me and gets the iPhone or they ship nothing.

[^1]: used to have a colored text in terminal when the product is released.
