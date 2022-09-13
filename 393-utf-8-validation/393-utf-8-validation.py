class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        n_bytes = 0

        for num in data:

            bnum = format(num, '#010b')[-8:]
            print(bnum)
            if n_bytes == 0:

                for bit in bnum:
                    if bit == '0': break
                    n_bytes += 1

                if n_bytes == 0:
                    continue

                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:

                if not (bnum[0] == '1' and bnum[1] == '0'):
                    return False

            n_bytes -= 1

        return n_bytes == 0     