def xgboost_bayesian_selector(n_estimators, learning_rate, max_depth, min_child_weight, subsample, colsample_bynode):

    model = XGBRegressor(
        random_state=0,
        n_estimators=int(n_estimators),
        learning_rate=learning_rate,
        max_depth=int(max_depth),
        min_child_weight=int(min_child_weight), 
        subsample=subsample,
        colsample_bynode=colsample_bynode
    )

    model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)
    y_pred = model.predict(X_test)
    result = mean_squared_error(y_test, y_pred, squared=False)

    return -result

    pbounds = {
        "n_estimators": (500, 2500),
        "learning_rate": (0.00001, 0.1),
        "max_depth": (1, 8),
        "min_child_weight": (1, 6),
        "subsample": (0.01, 0.9),
        "colsample_bynode": (0.01, 0.90)
    }

optimizer = BayesianOptimization(f=xgboost_bayesian_selector, pbounds=pbounds, verbose=2, random_state=0)
optimizer.maximize(init_points=2, n_iter=15)

print("Best result: {}; f(x) = {}.".format(optimizer.max["params"], optimizer.max["target"]))