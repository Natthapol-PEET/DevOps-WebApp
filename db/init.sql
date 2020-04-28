CREATE DATABASE coffee_shop;

use coffee_shop;

CREATE TABLE coffee_data (
prod_id 	varchar(10) NOT NULL PRIMARY KEY,
name  		varchar(40) NOT NULL ,
price   	INT NOT NULL,
type   		varchar(40) NOT NULL,
des   		varchar(100) NOT NULL,
path_img  	varchar(100) NOT NULL
) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("1001", "Iced Black Tea", 35, "cool", "flavor of tea the origin one. The oldest tea in the world discovered in china", "static/coffeeimg/cool/blackicetea.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("1002", "Ice Green Tea", 35, "cool", "imagine flavor of tea but put some mellow to it . Then you get green tea", "static/coffeeimg/cool/greentea.png");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("1003", "Ice Cocoa", 30, "cool", "the old cocoa with some cool in it make it so much better.", "static/coffeeimg/cool/icecocoa.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("1004", "Ice Coffee", 35, "cool", "when outside is too hot. but you have to get to work or focus this is your solution", "static/coffeeimg/cool/icecoffee.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("1005", "Ice Milk Tea", 35, "cool", "the flavor of milk but have some cool in it.", "static/coffeeimg/cool/icemilktea.png");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("1006", "Ice Lemon Tea", 35, "cool", "tasty sour flavor with some cool in it.", "static/coffeeimg/cool/lemonicetea.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("1007", "Ice black coffee", 30, "cool", "Bitter, refreshing flavor with some cool in it", "static/coffeeimg/cool/oleay.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("1008", "Iced Pink Milk", 35, "cool", "flavor of milk but more sweete then the origin one", "static/coffeeimg/cool/pinkmilk.jpg");

INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("2001", "Decaf Coffee", 45, "hot", "coffee that decreased caffeine", "static/coffeeimg/hot/decaf.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("2002", "French Press", 40, "hot", "coffee that press french style", "static/coffeeimg/hot/fr.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("2003", "Hot Cappuccino", 45, "hot", "coffee with some milk", "static/coffeeimg/hot/hot-cappuccino.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("2004", "Hot Cocoa", 45, "hot", "cocoa that make your morning better", "static/coffeeimg/hot/hot-cocoa.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("2005", "Hot Expresso", 45, "hot", "hot bitter flavor that will refreshing your day", "static/coffeeimg/hot/hot-expresso.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("2006", "Hot Green tea", 45, "hot", "a bitter flavor and smooth feeling", "static/coffeeimg/hot/hot-green-tea.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("2007", "Hot latte", 35, "hot", "coffee with some milk bubble.", "static/coffeeimg/hot/latte.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("2008", "Macchiato", 35, "hot", "underrated coffee ever . But it the most iconic one ", "static/coffeeimg/hot/macchiato.jpg");

INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("3001", "Americano Smoothie", 45, "smoothie", "smells strong coffee make it refreshing, with a bitter flavor", "static/coffeeimg/smoothie/americano.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("3002", "Cappucino Smoothie", 40, "smoothie", "coffee with some milk make it smooth and even smoother when making it a smoothie", "static/coffeeimg/smoothie/cappuccino.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("3003", "Cocoa Smoothie", 45, "smoothie", "sweet and bitter flavor, smoothie makes it a smooth feeling", "static/coffeeimg/smoothie/cocoashake.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("3004", "Espresso Smoothie", 45, "strong coffee flavor ", "static/coffeeimg/smoothie/expresso.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("3005", "Green Tea Smoothie", 45, "smoothie", "bitter and smooth flavor", "static/coffeeimg/smoothie/Green-smoothie.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("3006", "Milk Smoothie", 45, "smoothie", "milk flavor with some more smooth when making it a smoothie", "static/coffeeimg/smoothie/milk-smoothie.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("3007", "Mocha Smoothie", 35, "smoothie", "cocoa with coffee, sweet bitter add some more bitter and refreshing with coffee ", "static/coffeeimg/smoothie/mocha.jpg");
INSERT INTO coffee_data (prod_id, name, price, type, des, path_img)
VALUES ("3008", "Thai Milk Tea Smoothie", 35, "smoothie", "tea with some milk", "static/coffeeimg/smoothie/thai-milk-tea.jpg");



CREATE TABLE user (
uid         varchar(10) NOT NULL PRIMARY KEY,
address     varchar(100) NOT NULL,
passwd      varchar(20) NOT NULL,
name        varchar(40) NOT NULL,
tel_user    varchar(20) NOT NULL
) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

INSERT INTO user (uid, address, passwd, name, tel_user)
VALUES ("peet123", "83/3 Kud Khanuan Bungkaew Subdistrict Non Sa-at District Udon Thani Province 41240", "natthapol123", "natthapol  nonthasri", "0931851721");

INSERT INTO user (uid, address, passwd, name, tel_user)
VALUES ("peng123", "7/3 ban buangdanag patumrat roi-et 45190 ", "anaphut123", "anaphut rattanakham", "0649724822");

INSERT INTO user (uid, address, passwd, name, tel_user)
VALUES ("tong123", "8/3 ban nuang jonggram hell 5555", "natthapol666", "natthapol", "0666131313");


CREATE TABLE chart_data (
prod_id         varchar(10) NOT NULL,
uid              varchar(10) NOT NULL,
quantity         INT NOT NULL
) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

INSERT INTO chart_data (prod_id, uid, quantity) VALUES ("1001", "peet123", 1);
INSERT INTO chart_data (prod_id, uid, quantity) VALUES ("1002", "peet123", 2);


CREATE TABLE order_hist (
date	     TIMESTAMP,
prod_id      varchar(10) NOT NULL,
profit       INT NOT NULL,
user_id      varchar(10) NOT NULL,
bill_id      varchar(10) NOT NULL
) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

# CURRENT_TIMESTAMP
# SELECT TIMESTAMP("2017-04-26 22:11:11")
INSERT INTO order_hist (date, prod_id, profit, user_id, bill_id)
VALUES ("2020-04-26 15:53:00", "1001", 35, "peet123", "00123");
INSERT INTO order_hist (date, prod_id, profit, user_id, bill_id)
VALUES ("2020-04-27 16:40:00", "2001", 85, "peng123", "00335");
INSERT INTO order_hist (date, prod_id, profit, user_id, bill_id)
VALUES ("2020-04-27 16:40:00", "2002", 85, "peng123", "00335");
INSERT INTO order_hist (date, prod_id, profit, user_id, bill_id)
VALUES ("2020-04-28 10:59:00", "3007", 70, "tong123", "00666");
INSERT INTO order_hist (date, prod_id, profit, user_id, bill_id)
VALUES ("2020-04-28 10:59:00", "1001", 70, "tong123", "00666");


CREATE TABLE bill (
bill_id     varchar(10) NOT NULL PRIMARY KEY,
balance      INT NOT NULL
) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

INSERT INTO bill (bill_id, balance) VALUES ("00123", 120);
