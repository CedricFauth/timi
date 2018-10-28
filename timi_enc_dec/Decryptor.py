class Decryptor:


    def run(self, message):
        border = len(message)
        #print(border)
        while True:
            rightside = len(message[border:])
            leftside = 0
            i= 2
            if border <= i:
                return self.error("border <= i")
            else:
                while True:
                    #print(message[i])
                    leftside += int(message[i])

                    if i+3 >= border:
                        break
                    i +=3

            if leftside > rightside:
                border -=1
            elif leftside == rightside:
                break
            else:
                return self.error("no solution")
            #print(border)

        position = list(message[border:])
        quantity = []
        numbers_no_doubles = []

        for i in range(int((len(message)-rightside)/3)):
            numbers_no_doubles.append(message[3*i:3*i+2])
            quantity.append(message[3*i+2])
        #print(numbers_no_doubles)
        #print(quantity)

        numbers_with_doubles = []
        for count in range(len(quantity)):
            for repetations in range(int(quantity[count])):
                numbers_with_doubles.append(numbers_no_doubles[count])
        #print(numbers_with_doubles)

        message_in_letters = self.numbers_to_abc(numbers_with_doubles)

        #print(position)

        output_message_list = [""] * len(message_in_letters)
        for letter_index in range(len(position)):
            output_message_list[int(position[letter_index])-1] = message_in_letters[letter_index]
        output_message = ''.join(output_message_list)
        return output_message

    def numbers_to_abc(self, message):
        abc_dict = {"01": "A", "02": "B", "03": "C", "04": "D", "05": "E", "06": "F",
                    "07": "G", "08": "H", "09": "I", "10": "J", "11": "K", "12": "L",
                    "13": "M", "14": "N", "15": "O", "16": "P", "17": "Q", "18": "R",
                    "19": "S", "20": "T", "21": "U", "22": "V", "23": "W", "24": "X",
                    "25": "Y", "26": "Z", "27": "a", "28": "b", "29": "c", "30": "d",
                    "31": "e", "32": "f", "33": "g", "34": "h", "35": "i", "36": "j",
                    "37": "k", "38": "l", "39": "m", "40": "n", "41": "o", "42": "p",
                    "43": "q", "44": "r", "45": "s", "46": "t", "47": "u", "48": "v",
                    "49": "w", "50": "x", "51": "y", "52": "z", "53": "ä", "54": "ö",
                    "55": "ü", "56":" "}
        message_in_letters = []
        for i in message:
            message_in_letters.append(abc_dict[i])
        return message_in_letters

    def error(self, errortype):
        return "error: " + errortype



#27102103105208109212148279361500272011031041081091141221168425397000110511924132