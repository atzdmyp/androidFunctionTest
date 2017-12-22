
from time import sleep
from testSet.common import common as common
from testSet.common.common import Element
import testSet.common.Log as Log
log = Log.MyLog.get_log()
logger = log.get_my_logger()


def open_app():
    """
    open the app,enter the index
    :return:
    """

    logger.info("Begin open the app")
    # skip
    if Element("GuideActivity", "Guide").is_exist():

        logger.info("Click skin button")
        Element("GuideActivity", "skip").click()

    # welcome
    if Element("GuideActivity", "welcome").is_exist():

        logger.info("Gide page--swip right")
        while not Element("GuideActivity", "goShop").is_exist():

            # swip right
            common.my_swipe_to_right()
            sleep(1)
        else:
            Element("GuideActivity", "goShop").click()

    # loading
    wait_loading()

    # update
    if Element("Alert", "cancel").is_exist():
        Element("Alert", "cancel").click()

    # loading
    wait_loading()

    logger.info("End open the app")


def cancel_update():
    if Element("Alert", "update_title").is_exist():
        Element("Alert", "cancel").click()
    else:
        pass


def login(email, password):
    """
    login app
    :return:
    """
    # cancel for update
    cancel_update()

    logger.info("Begin login the app")
    if Element("BottomNavigation", "BottomNavigation").is_exist():
        logger.debug("Current is already login, first logout")

        logout()

        logger.debug("Begin login")
    else:
        pass
        # Element("profile", "SignIn").click()
        # wait_loading()
    if Element("login", "fblogin").is_exist():
        login_input(email, password)

    else:
        Element("login", "loginText").click()
        login_input(email, password)

    logger.info("End login the app")


def login_input(email, password):
    """
    input email and password for login
    :param email:
    :param password:
    :return:
    """
    if Element("login", "fblogin").is_exist():
        # input email
        Element("login", "mail").send_keys(0, email)

        # input password
        Element("login", "password").send_keys(0, password)

        # click sign in button
        Element("login", "signIn").click()


def register_input(email, password):
    """
    input email and password for register
    :param email:
    :param password:
    :return:
    """
    if Element("register", "fbregister").is_exist():
        # input email
        Element("register", "re_email").send_keys(0, email)

        # input password
        Element("register", "re_pass").send_keys(0, password)

        # click sign in button
        Element("register", "register").click()


def input_address(first_name, last_name, phone, zip_code, address_1, address_2, city, country, state):
    """
        input elements for address
        :param first_name:
        :param last_name:
        :param phone:
        :param zip_code:
        :param address_1:
        :param address_2:
        :param city:
        :param country:
        :param state:
        :return:
        """
    # enter given name
    Element("Address", "edit_elements").send_keys(0, first_name)
    # enter surname
    Element("Address", "edit_elements").send_keys(1, last_name)
    # enter phone
    Element("Address", "edit_elements").send_keys(2, phone)
    # enter zip code
    Element("Address", "edit_elements").send_keys(3, zip_code)
    # enter address line1
    Element("Address", "edit_elements").send_keys(4, address_1)
    # enter address line2
    Element("Address", "edit_elements").send_keys(5, address_2)
    # enter city
    Element("Address", "edit_elements").send_keys(6, city)
    # enter country
    if country != "":
        Element("Address", "edit_elements").clicks(7)
        sleep(1)
        i = int(country)
        Element("Address", "country_list").clicks(i)
    # enter state/province
    if country == "0" and country == "7" and country == "8":
        j = int(state)
        Element("Address", "country_list").clicks(j)
    else:
        Element("Address", "edit_elements").send_keys(8, state)
    # click done button
    Element("Address", "done_btn").click()


def go_to_me():
    """
    go to consumer center
    :return:
    """
    if Element("BottomNavigation", "BottomNavigation").is_exist():

        if Element("BottomNavigation", "ME").is_exist():
            bar_me = Element("BottomNavigation", "ME").gets(4)
            bar_me.click()


def go_to_category():
    """
    go to category
    :return:
    """
    if Element("BottomNavigation", "BottomNavigation").is_exist():

        if Element("BottomNavigation", "CATEGORY").is_exist():
            bar_me = Element("BottomNavigation", "CATEGORY").gets(1)
            bar_me.click()


def go_to_setting():
    """
    go to setting
    :return:
    """
    go_to_me()
    if not Element("loginOut", "setting").does_exist():
        return False
    else:
        Element("loginOut", "setting").click()

    return True


def logout():
    """
    logout the app
    :return:
    """
    # if already sign in , first sign out
    # join personal center
    if go_to_setting():
        while not Element("loginOut", "loginOut").is_exist():
            # swipe up
            common.my_swipe_to_up()
        else:

            logger.debug("Begin logout")
            Element("loginOut", "loginOut").click()

            if Element("Alert", "confirm").is_exist():
                Element("Alert", "confirm").click()

            wait_loading()
            logger.debug("End logout")


def register(email, password):
    """
    register
    :return:
    """
    logger.info("Begin register the app")
    if Element("BottomNavigation", "BottomNavigation").is_exist():

        logger.debug("Current is already login, first logout")

        logout()

        logger.debug("Begin login")
        # Element("profile", "SignIn").click()
        # wait_loading()
    if not Element("register", "fbregister").is_exist():
        Element("register", "registerText").click()
        register_input(email, password)

    else:
        register_input(email, password)

    logger.info("End register the app")


def return_index():
    """
    return then index
    :return:
    """

    # Determine whether there is BottomNavigation
    logger.info("Determine whether there is BottomNavigation")
    while not Element("BottomNavigation", "BottomNavigation").is_exist():

        # key event:back
        logger.info("Key event:back")
        common.back()

        sleep(1)
        if Element("BottomNavigation", "BottomNavigation").is_exist():
                break

        logger.info("Swipe down")
        common.my_swipe_to_down()

        sleep(1)
        if Element("BottomNavigation", "BottomNavigation").is_exist():
                break

    # click the shop button
    Element("BottomNavigation", "SHOP").gets(0).click()

    wait_loading()


def enter_cart():
    """
    enter the shopping cart
    :return:
    """
    logger.info("Enter add cart page")
    if not Element("Good_details", "add").is_exist():
        common.my_swipe_to_up()
    else:
        Element("Good_details", "add").click()


def add_goods_in_cart(num):
    """
     add goods to cart
    :param num: goods number
    :return:
    """

    if num == 0:
        return

    goods_name_list = []

    for i in range(num):

        if Element("BottomNavigation", "BottomNavigation").is_exist():
            common.my_swipe_to_up()

        while not Element("Shop", "goods").is_exist():
            common.my_swipe_to_up()
        else:
            Element("Shop", "goods").clicks(i)

            goods_name = Element("title", "title").get_attribute("text")

            goods_name_list.append(goods_name)

            enter_cart()

            if Element("add_cart", "add_cart").does_exist():

                logger.info("Select size")
                Element("add_cart", "size").clicks(0)

            Element("add_cart", "done").click()
        logger.info("Return index")
        return_index()
    return goods_name_list


def delete_goods_in_cart(goods_name):
    """
    delete goods in shopping cart
    :param goods_name: you need delete goods's name
    :return:
    """
    logger.info("Delete the goods which we choose")
    goods_list = []

    logger.info("Determine whether there is a goods")
    while Element("Shopping_cart", "goods_name").is_exist():

        logger.info("Get the goods name")
        element_list = Element("Shopping_cart", "goods_name").get_element_list()

        if element_list is not None:

            logger.info("Get the last goods name")
            last_goods_name = element_list[-1].get_attribute("text")

            for i in range(len(element_list)):

                value = element_list[i].get_attribute("text")

                if value == goods_name:

                    logger.info("Delete goods")

                    Element("Shopping_cart", "delete_goods").clicks(i)

                    Element("Alert", "confirm").click()

                    wait_loading()

                    return

        if last_goods_name not in goods_list:

            logger.info("Goods is not end")

            logger.info("Swipe up, if not end")

            common.my_swipe_to_up()

            goods_list.append(last_goods_name)
        else:
            logger.info("Goods is end")
            return


def clear_cart():
    """
    clear the shopping cart
    :return:
    """
    logger.info("Clear the shopping cart")
    goods_list = []
    while Element("Shopping_cart", "goods_name").is_exist():
        logger.info("Get the goods name")
        element_list = Element("Shopping_cart", "goods_name").get_element_list()

        if element_list is not None:
            last_goods_name = element_list[-1].get_attribute("text")

            for i in range(len(element_list)):
                logger.info("Delete goods")

                Element("Shopping_cart", "delete_goods").clicks(i)

                Element("Alert", "confirm").click()

                wait_loading()
        if last_goods_name not in goods_list:

            logger.info("Goods is not end")

            logger.info("Swipe up, if not end")

            common.my_swipe_to_up()

            goods_list.append(last_goods_name)
        else:
            logger.info("Goods is end")
            break


def get_total_price_in_cart():
    """
    get the all goods price in shopping cart
    :return:
    """
    logger.info("Determine whether there is a goods")
    goods_list = []
    total_price = 0
    while Element("Shopping_cart", "goods_name").is_exist():
        logger.info("Get the goods name")
        element_list = Element("Shopping_cart", "goods_name").get_element_list()

        if element_list is not None:

            logger.info("Get the last goods name")
            last_goods_name = element_list[-1].get_attribute("text")

            for i in range(len(element_list)):

                goods_name = element_list[i].get_attribute("text")

                if goods_name not in goods_list:
                    goods_list.append(goods_name)

                    goods_price_text = Element("Shopping_cart", "goods_price").gets(i).get_attribute("text")
                    goods_price = goods_price_text[goods_price_text.find("$")+1:]
                    goods_num = Element("Shopping_cart", "goods_num").gets(i).get_attribute("text")

                    one_goods_price = float(goods_price)*int(goods_num)
                    total_price += one_goods_price

            if last_goods_name not in goods_list:

                logger.info("Goods is not end")

                logger.info("Swipe up, if not end")

                common.my_swipe_to_up()

                goods_list.append(last_goods_name)
            else:
                logger.info("Goods is end")
                break
    return str(total_price)


def add_address_in_checkout(first_name, last_name, phone, zip_code, address_1, address_2, city, country, state):
    """
    Add address while there have no address
    :param first_name:
    :param last_name:
    :param phone:
    :param zip_code:
    :param address_1:
    :param address_2:
    :param city:
    :param country:
    :param state:
    :return:
    """
    if not Element("checkout", "ad_name") and Element("checkout", "ad_address").is_exist():
        logger.info("No shipping address and billing address.")
        logger.info("Start to add address.")
        Element("checkout", "ship_edit").click()
        input_address(first_name, last_name, phone, zip_code, address_1, address_2, city, country, state)
    else:
        logger.info("Always has a address.")


def choose_shipping_payment_methods_in_checkout(shipping_method, payment_method):
    """
    choose method for shipping and payment
    :param shipping_method:
    :param payment_method:
    :return:
    """
    # choose shipping method
    shipping_methods = Element("checkout", "shopping_method").get_element_list()
    if shipping_methods is not None:
        methods = []
        for i in range(len(shipping_methods)):
            methods[i] = shipping_methods[i].get_attribute("text")
            if methods[i] is not None:
                if methods[i] == shipping_method:
                    logger.info("Choose the shipping method is:" + shipping_method)
                    Element("checkout", "shopping_method").gets(i).click()
    else:
        logger.info("The shipping method is none!")

    # choose payment method
    if not Element("checkout", "payment_method").is_exist():
        common.my_swipe_to_up()
    else:
        payment_methods = Element("checkout", "payment_method").get_element_list()
        if payment_methods is not None:
            payments = []
            for i in range(len(payment_methods)):
                payments[i] = payment_methods[i].get_attribute("text")
                if payments[i] == payment_method:
                    logger.info("Choose the payment method is:" + payment_method)
                    Element("checkout", "payment_method").gets(i).click()
        else:
            logger.info("The payment method is none!")


def input_coupon_code(coupon_code):
    """
    input the coupon code
    :param coupon_code:
    :return:
    """
    code_coupon = 0
    if not coupon_code == "":
        # enter coupon_code
        if not Element("checkout", "coupon_code").is_exist():
            common.my_swipe_to_up()
        else:
            Element("checkout", "coupon_code").click()
            wait_loading()
        Element("checkout", "coupon_freebie_input").send_key(coupon_code)
        sleep(1)
        Element("checkout", "coupon_freebie_save").click()
        if Element("Alert", "layout").is_exist():
            message = Element("Alert", "message").get_attribute("text")
            if message == "success":
                logger.info("Using coupon code that is \'" + coupon_code + "\' successfully!")
                Element("Alert", "confirm").click()
            else:
                logger.info("The \'" + coupon_code + "\' coupon code can not be used.")
                Element("Alert", "confirm").click()
                common.back()
                code_coupon = 1
    else:
        logger.info("Don't use coupon code.")
    return int(code_coupon)


def input_freebie(freebie):
    """
    input the freebie
    :param freebie:
    :return:
    """
    code_freebie = 0
    if not freebie == "":
        # enter freebie
        if not Element("checkout", "freebie").is_exist():
            common.my_swipe_to_up()
        else:
            Element("checkout", "freebie").click()
            wait_loading()
        Element("checkout", "coupon_freebie_input").send_key(freebie)
        sleep(1)
        Element("checkout", "coupon_freebie_save").click()
        if Element("Alert", "layout").is_exist():
            message = Element("Alert", "message").get_attribute("text")
            if message == "success":
                logger.info("Using \'" + freebie + "\' points successfully!")
                Element("Alert", "confirm").click()
            else:
                logger.info("No points in account, using points failed.")
                Element("Alert", "confirm").click()
                common.back()
                code_freebie = 1
    else:
        logger.info("Don't use shein points.")
    return int(code_freebie)


def get_total_price_in_checkout():
    """
    get the total price in checkout
    :return:total_price
    """
    total_price_text = Element("checkout", "total").get_attribute("text")
    total_price = total_price_text[total_price_text.find("$")+1:]
    return float(total_price)


def get_subtotal_price_in_checkout():
    """
    get the subtotal price in checkout
    :return:subtotal_price
    """
    subtotal_price_text = Element("checkout", "subtotal").get_attribute("text")
    subtotal_price = subtotal_price_text[subtotal_price_text.find("$")+1:]
    return float(subtotal_price)


def get_coupon_code_price_in_checkout():
    """
    get the coupon code price in checkout
    :return:coupon_code_price
    """
    coupon_code_price_text = Element("checkout", "coupon_code_price").get_attribute("text")
    coupon_code_price = coupon_code_price_text[coupon_code_price_text.find("$")+1:]
    return float(coupon_code_price)


def get_freebie_price_in_checkout():
    """
    get the freebie price in checkout
    :return:freebie_price
    """
    freebie_price_text = Element("checkout", "freebie_price").get_attribute("text")
    freebie_price = freebie_price_text[freebie_price_text.find("$")+1:]
    return float(freebie_price)


def get_shipping_price_in_checkout():
    """
    get the shipping price in checkout
    :return: shipping_price
    """
    shipping_price_text = Element("checkout", "shipping_price").get_attribute("text")
    shipping_price = shipping_price_text[shipping_price_text.find("$")+1:]
    return float(shipping_price)


def input_card_paypal_message_in_payment(payment_method, card_no, cvv):
    code = True
    title = Element("shippinginfo", "shipping_info_title").get_attribute("text")
    if title == "Payment":
        # Credit Card payment
        if payment_method == "Credit Card":
            # enter card number
            if not Element("payment", "card_number").is_exist():
                common.my_swipe_to_up()
            else:
                Element("payment", "card_number").send_key(card_no)
                # enter expire date
            if not Element("payment", "expire_date_month").is_exist():
                common.my_swipe_to_up()
            else:
                Element("payment", "expire_date_month").click()
                sleep(1)
                if Element("payment", "expire_date_dialog").is_exist():
                    Element("payment", "months").clicks(8)
                else:
                    logger.info("No month can be chosen.")
            if not Element("payment", "expire_date_year").is_exist():
                common.my_swipe_to_up()
            else:
                Element("payment", "expire_date_year").click()
                sleep(1)
                if Element("payment", "expire_date_dialog").is_exist():
                    Element("payment", "years").clicks(3)
                else:
                    logger.info("No years can be chosen.")
            # enter cvv number
            if not Element("payment", "cvv_number").is_exist():
                common.my_swipe_to_up()
            else:
                Element("payment", "cvv_number").send_key(cvv)
            # click purchase
            if not Element("payment", "purchase").is_exist():
                common.my_swipe_to_up()
            else:
                Element("payment", "purchase").click()
                wait_loading()
                result = Element("shippinginfo", "shipping_info_title").get_attribute("text")
                if str(result) != "PAYMENT SUCCESS":
                    logger.info("Pay fail.")
                    code = False
        # PayPal payment
        elif payment_method == "PayPal":
            title = Element("shippinginfo", "shipping_info_title").get_attribute("text")
            if not title == "Payment":
                code = False
    else:
        logger.info("This is not the payment page.")
        code = False
    return code


def wait_loading():
    """
    Waiting for the end of the page load
    :return:
    """
    # loading img
    while Element("Alert", "loading").is_exist():
        sleep(1)
    else:
        # time out
        if Element("Alert", "confirm").is_exist():
            Element("Alert", "confirm").click()


def get_login_cls():
    """
    get login cls
    :return: login_cls

    login_cls : [[case_name,user_name,password,result,message],]
    """

    login_cls = common.get_xls("romwe_login")

    return login_cls


def get_register_cls():
    """
    get register cls
    :return:register_cls

    register_cls : [[case_name,user_name,password,result,message],]
    """

    register_cls = common.get_xls("romwe_register")

    return register_cls


def get_address_cls():

    address_cls = common.get_xls("romwe_address")

    return address_cls


def get_change_password_cls():
    change_password_cls = common.get_xls("romwe_pass")

    return change_password_cls


def get_add_cart_cls():
    add_cart_cls = common.get_xls("add_cart")

    return add_cart_cls


def get_write_review_cls():
    write_review_cls = common.get_xls("add_cart")

    return write_review_cls


def get_feed_back_cls():
    feed_back_cls = common.get_xls("romwe_feedback")

    return feed_back_cls


def get_tickets_cls():
    my_tickets_cls = common.get_xls("romwe_tickets")

    return my_tickets_cls


def get_checkout_cls():
    my_checkout_cls = common.get_xls("romwe_checkout")

    return my_checkout_cls

if __name__ == '__main__':
    print(get_login_cls())
