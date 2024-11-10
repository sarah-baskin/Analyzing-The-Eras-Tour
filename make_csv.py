import os
import csv
import songs_excl_ftv as song_list

def create_csv(input, output):
    with open(output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for root in os.walk(song_list):
            print(root)

        # for filename in os.listdir(input):
        #         file_path = os.path.join(input, filename)
        #         print(file_path)

                # if os.path.isfile(file_path):
                #     with open(file_path, 'r') as file:
                #         content = file.read()
                #         writer.writerow([filename, content])

if __name__ == "__main__":
    input = song_list
    output = 'songs_excl_ftv.csv'
    create_csv(input, output)