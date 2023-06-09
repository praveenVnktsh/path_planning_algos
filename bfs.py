import cv2
import numpy as np
import imageio

images =[ ]
def draw(mat, start, goal, drawfinal = False):
    m = mat.copy()
    m[start[0]][start[1]] = 3
    m[goal[0]][goal[1]] = 3

    images.append(cv2.resize(m * 80, (150, 150), interpolation = cv2.INTER_NEAREST))
    cv2.imshow("BFS", images[-1])
    if cv2.waitKey(1) == ord('q'):
        exit()

def bfs(mat, start, end):
    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(start)
    mat[start[0]][start[1]] = 2

    while queue:
        # Dequeue a vertex from queue
        s = queue.pop(0)
        
        # If this adjacent node is the destination node,
        # then return true
        if s == end:
            return True

        # Get all adjacent vertices of the dequeued vertex s.
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        if s[0] < len(mat) - 1 and mat[s[0] + 1][s[1]] == 0:
            mat[s[0] + 1][s[1]] = 2
            queue.append((s[0] + 1, s[1]))
        if s[0] > 0 and mat[s[0] - 1][s[1]] == 0:
            mat[s[0] - 1][s[1]] = 2
            queue.append((s[0] - 1, s[1]))
        if s[1] < len(mat[0]) - 1 and mat[s[0]][s[1] + 1] == 0:
            mat[s[0]][s[1] + 1] = 2
            queue.append((s[0], s[1] + 1))
        if s[1] > 0 and mat[s[0]][s[1] - 1] == 0:
            mat[s[0]][s[1] - 1] = 2
            queue.append((s[0], s[1] - 1))

        # cv2.imshow("BFS", cv2.resize(mat * 127, (500, 500), interpolation = cv2.INTER_NEAREST))
        # cv2.waitKey(100)
        draw(mat, start, end)
    
    return False

if __name__ == "__main__":

    # mat = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    # ]
    mat = np.random.randn(30, 30).astype(np.uint8)
    thresh = 0.9
    newmat = mat.copy()
    newmat[mat > thresh] = 1
    newmat[mat <= thresh] = 0
    start = (mat.shape[0]//2 - 1, mat.shape[1]//2 - 1)
    end = (mat.shape[0] - 1, mat.shape[1] - 1)
    
    newmat[start[0]][start[1]] = 0
    newmat[end[0]][end[1]] = 0
    (bfs(newmat, start, end))

    # cv2.imshow("BFS", cv2.resize(mat * 127, (500, 500), interpolation = cv2.INTER_NEAREST))
    print('saving')
    imageio.mimwrite('gifs/bfs.gif', images, fps=60)