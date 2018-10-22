

password = "EECS388-";

alphabet = "0123456789abcdefghijklmnopqrstuvwxyz";


for i in alphabet:
    string = password;
    string += i;

    for j in alphabet:
        newstring = string;
        newstring += j;

        for k in alphabet:
            final = newstring;
            final += k;
            print(final);
