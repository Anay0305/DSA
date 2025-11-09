class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        x_cords = [0] * (n + 1)
        y_cords = [0] * (n + 1)
        last_cord = [0, 0]
        for i, val in enumerate(s):
            if val == 'U' or val == 'D':
                x_cords[i + 1] = x_cords[i]
                if val == 'U':
                    last_cord[1] = last_cord[1] + 1
                    y_cords[i + 1] = last_cord[1]
                elif val == 'D':
                    last_cord[1] = last_cord[1] - 1
                    y_cords[i + 1] = last_cord[1]
            if val == 'L' or val == 'R':
                y_cords[i + 1] = y_cords[i]
                if val == 'L':
                    last_cord[0] = last_cord[0] - 1
                    x_cords[i + 1] = last_cord[0]
                elif val == 'R':
                    last_cord[0] = last_cord[0] + 1
                    x_cords[i + 1] = last_cord[0]
        res = set()
        final_cord = (x_cords[-1], y_cords[-1])
        for i in range(0, n - k + 1):
            cur_x_cord = final_cord[0] - (x_cords[i + k] - x_cords[i])
            cur_y_cord = final_cord[1] - (y_cords[i + k] - y_cords[i])
            res.add((cur_x_cord, cur_y_cord))

        return len(res)