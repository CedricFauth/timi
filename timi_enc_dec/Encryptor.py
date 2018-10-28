
class Encryptor:


    def run(self, message):

        sorted_word, position = self.sort(message)

        sorted_word_removed_doubles, quantity = self.delete_doubles_and_give_quantity(sorted_word)

        try:
            sorted_numbers = self.abc_to_numbers(sorted_word_removed_doubles)
        except KeyError:
            return "error: unknown letters"

        output = ""
        for i1 in range(len(sorted_numbers)):
            output += sorted_numbers[i1] + str(quantity[i1])
        output += str(position).strip('[]').replace(", ","")

        return(output)


    def sort(self, inp):
        inp = list(inp)
        position = list(range(1, len(inp) + 1))
        #print(inp, position)
        for i in range(len(inp)):
            for num in range(len(inp)):
                if inp[i] < inp[num]:
                    inp[i], inp[num] = inp[num], inp[i]
                    position[i],position[num] = position[num],position[i]
        #print(inp, position)

        return inp,position


    def delete_doubles_and_give_quantity(self, sorted_word):
        quantity = []
        sorted_word_removed_doubles = []
        for index in range(len(sorted_word)):
            #print(index)
            if index == 0:
                quantity.append(1)
                sorted_word_removed_doubles.append(sorted_word[index])
            else:
                if sorted_word[index] == sorted_word[index - 1]:
                    quantity[len(quantity)-1] += 1
                else:
                    quantity.append(1)
                    sorted_word_removed_doubles.append(sorted_word[index])
        return sorted_word_removed_doubles, quantity


    def abc_to_numbers(self, message):
        number_dict = {"A": "01", "B": "02", "C": "03", "D": "04", "E": "05", "F": "06",
                       "G": "07", "H": "08", "I": "09", "J": "10", "K": "11", "L": "12",
                       "M": "13", "N": "14", "O": "15", "P": "16", "Q": "17", "R": "18",
                       "S": "19", "T": "20", "U": "21", "V": "22", "W": "23", "X": "24",
                       "Y": "25", "Z": "26", "a": "27", "b": "28", "c": "29", "d": "30",
                       "e": "31", "f": "32", "g": "33", "h": "34", "i": "35", "j": "36",
                       "k": "37", "l": "38", "m": "39", "n": "40", "o": "41", "p": "42",
                       "q": "43", "r": "44", "s": "45", "t": "46", "u": "47", "v": "48",
                       "w": "49", "x": "50", "y": "51", "z": "52", "ä": "53", "ö": "54",
                       "ü": "55", " ": "56"}
        message_in_numbers = []
        for i in message:
            message_in_numbers.append(number_dict[i])
        return message_in_numbers
