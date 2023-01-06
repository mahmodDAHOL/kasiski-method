from collections import Counter
import math
import typer


def get_number_of_repeat_of_segment_in_text(text, seg):
    rep = 0
    index = []
    for i, letter in enumerate(text):
        if letter == seg[0]:
            if text[i:i+len(seg)] == seg:
                rep += 1     
                index.append(i)
    return rep, index
def get_difference_for_first_appearence_and_second_appearence(seg_reps):
    diffs = []
    for seg_rep in seg_reps:
        if len(seg_reps[seg_rep]) >= 2:
            diff = seg_reps[seg_rep][1] - seg_reps[seg_rep][0]
            diffs.append(diff)
    return diffs


def main(cipher_text: str = typer.Option(..., prompt=True),
         max_key_len: int = typer.Option(..., prompt=True)
         ):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    inv_alpha = dict()
    for i,ch in enumerate(alphabets):
        inv_alpha[i] = ch


    for seg_len in range(2, max_key_len):
        seg_reps = {}

        for i in range(len(cipher_text) // seg_len):
            seg = cipher_text[i:i+seg_len]
            rep, index = get_number_of_repeat_of_segment_in_text(cipher_text, seg)
            seg_reps[seg] = index

        diffs = get_difference_for_first_appearence_and_second_appearence(seg_reps)
        key_len = math.gcd(*diffs)
        c_list = []
        for i in range(key_len):
            c = cipher_text[i::key_len]
            c_list.append(c)
        key = ""
        for c in c_list:
            most_common_letter = Counter(c).most_common(1)[0][0]    
            key += inv_alpha[abs(ord(most_common_letter) - ord("e"))]
        if key:
            print(f"{seg_len=} => {key=}" )
        
            

if __name__ == "__main__":
    typer.run(main)