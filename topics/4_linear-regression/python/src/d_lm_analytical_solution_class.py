# d_lm.py

import numpy as np
import scipy.stats as stats

def d_lm(x, y, confidence=0.95):
    n = len(x)

    x_bar = np.mean(x)
    y_bar = np.mean(y)

    S_yx = np.sum((y - y_bar) * (x - x_bar))
    S_xx = np.sum((x - x_bar)**2)

    # ====== estimate beta_0 and beta_1 ======
    beta_1_hat = S_yx / S_xx # also equal to (np.cov(x, y))[0, 1] / np.var(x)
    beta_0_hat = y_bar - beta_1_hat * x_bar

    # ====== estimate sigma ======
    # residual
    y_hat = beta_0_hat + beta_1_hat * x
    r = y - y_hat
    sigma_hat = np.sqrt(sum(r**2) / (n-2))

    # ====== estimate sum of squares ======
    # total sum of squares
    SS_total = np.sum((y - y_bar)**2)
    # regression sum of squares
    SS_reg = np.sum((y_hat - y_bar)**2)
    # residual sum of squares
    SS_err = np.sum((y - y_hat)**2)

    # ====== estimate R2: coefficient of determination ======
    R2 = SS_reg / SS_total

    # ====== R2 = correlation_coefficient**2 ======
    correlation_coefficient = np.corrcoef(x, y)
    delta = correlation_coefficient[0, 1]**2 - R2

    # ====== estimate MS ======
    # sample variance
    MS_total = SS_total / (n-1)
    MS_reg = SS_reg / 1.0
    MS_err = SS_err / (n-2)

    # ====== estimate F statistic ======
    F = MS_reg / MS_err
    F_test_p_value = 1 - stats.f._cdf(F, dfn=1, dfd=n-2)

    # ====== beta_1_hat statistic ======
    beta_1_hat_var = sigma_hat**2 / ((n-1) * np.var(x))
    beta_1_hat_sd = np.sqrt(beta_1_hat_var)

    # confidence interval
    z = stats.t.ppf(q=0.025, df=n-2)
    beta_1_hat_CI_lower_bound = beta_1_hat - z * beta_1_hat_sd
    beta_1_hat_CI_upper_bound = beta_1_hat + z * beta_1_hat_sd

    # hypothesis tests for beta_1_hat
    # H0: beta_1 = 0
    # H1: beta_1 != 0
    beta_1_hat_t_statistic = beta_1_hat / beta_1_hat_sd
    beta_1_hat_t_test_p_value = 2 * (1 - stats.t.cdf(np.abs(beta_1_hat_t_statistic), df=n-2))

    # ====== beta_0_hat statistic ======
    beta_0_hat_var = beta_1_hat_var * np.sum(x**2) / n
    beta_0_hat_sd = np.sqrt(beta_0_hat_var)

    # confidence interval
    beta_0_hat_CI_lower_bound = beta_0_hat - z * beta_0_hat_sd
    beta_1_hat_CI_upper_bound = beta_0_hat + z * beta_0_hat_sd
    beta_0_hat_t_statistic = beta_0_hat / beta_0_hat_sd
    beta_0_hat_t_test_p_value = 2 * (1 - stats.t.cdf(np.abs(beta_0_hat_t_statistic), df=n-2))

    # confidence interval for the regression line
    sigma_i = 1.0/n * (1 + ((x - x_bar) / np.std(x))**2)
    y_hat_sd = sigma_hat * sigma_i

    y_hat_CI_lower_bound = y_hat - z * y_hat_sd
    y_hat_CI_upper_bound = y_hat + z * y_hat_sd

    lm_result = {}
    lm_result['beta_1_hat'] = beta_1_hat
    lm_result['beta_0_hat'] = beta_0_hat
    lm_result['sigma_hat'] = sigma_hat
    lm_result['y_hat'] = y_hat
    lm_result['R2'] = R2
    lm_result['F_statistic'] = F
    lm_result['F_test_p_value'] = F_test_p_value
    lm_result['MS_error'] = MS_err
    lm_result['beta_1_hat_CI'] = np.array([beta_1_hat_CI_lower_bound, beta_1_hat_CI_upper_bound])
    lm_result['beta_1_hat_standard_error'] = beta_1_hat_sd
    lm_result['beta_1_hat_t_statistic'] = beta_1_hat_t_statistic
    lm_result['beta_1_hat_t_test_p_value'] = beta_1_hat_t_test_p_value
    lm_result['beta_0_hat_standard_error'] = beta_0_hat_sd
    lm_result['beta_0_hat_t_statistic'] = beta_0_hat_t_statistic
    lm_result['beta_0_hat_t_test_p_value'] = beta_0_hat_t_test_p_value
    lm_result['y_hat_CI_lower_bound'] = y_hat_CI_lower_bound
    lm_result['y_hat_CI_upper_bound'] = y_hat_CI_upper_bound

    return lm_result