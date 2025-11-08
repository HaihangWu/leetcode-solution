import torch

points1 = torch.tensor([[0.0, 0.0], [1.0, 1.0]])
points2 = torch.tensor([[0.0, 0.0], [-1.0, -1.0]])

# Compute Euclidean distance (p=2.0)
distances = torch.cdist(points1, points2, p=2.0)
print(distances)