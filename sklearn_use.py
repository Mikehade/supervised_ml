from sklearn.linear_model import SGDRegressor

# Regressor
model = SGDRegressor(loss="squared_error")
# model = SGDRegressor(loss="huber")

# classification
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

from sklearn.metrics import log_loss
y_true = [1, 0, 1, 1]
y_pred = [0.9, 0.1, 0.8, 0.3]

print(log_loss(y_true, y_pred))