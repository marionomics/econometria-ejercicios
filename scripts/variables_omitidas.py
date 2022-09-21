def run():
    import numpy as np
    import pandas as pd

    np.random.seed(42)
    size = 25000

    df = pd.DataFrame({'education': np.random.normal(size = size),
                        'ability': np.random.normal(size = size)})

    df = (df-df.min())/(df.max()-df.min())
    df['education'] = df['education'] * 22
    df['income'] = 4000 + 1000 * df['education'] + 4000 * df['ability'] + np.random.normal(size = size)

    df.to_csv('data/simulations/education.csv')

    print(df.head())

if __name__ == "__main__":
    run()