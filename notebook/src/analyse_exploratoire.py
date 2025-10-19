def display_missing_values(df):
    # Calcul du pourcentage de valeurs manquantes pour chaque colonne
    missing_rate = (df.isnull().sum() / len(df)) * 100
    missing_rate = missing_rate.sort_values(ascending=False)
    
    # Séparer les variables selon leur type
    num_cols = df.select_dtypes(include=['number']).columns
    cat_cols = df.select_dtypes(exclude=['number']).columns

    print(" Variables NUMÉRIQUES")
    display(missing_rate[num_cols][missing_rate[num_cols] > 0])
    print("\n Variables CATÉGORIELLES ")
    display(missing_rate[cat_cols][missing_rate[cat_cols] > 0])

display_missing_values(df)
# Que pouvez-vous conclure ?

#3) Petite fonction générique
def impute_target_with_reg(df, target_col, features):
    # Sépare numériques et catégorielles dans les "features"
    num_feats = [c for c in features if c in num_cols_all]
    cat_feats = [c for c in features if c in cat_cols_all]

    # Lignes connues / manquantes
    known_idx = df[target_col].notna()
    miss_idx  = df[target_col].isna()
    
    out_col = f"{target_col}_imp_reg"
    df[out_col] = df[target_col]  # copie de la colonne originale
    if miss_idx.sum() == 0:
        return df  # rien à imputer

    X_train = df.loc[known_idx, num_feats + cat_feats]
    y_train = df.loc[known_idx, target_col]
    X_test  = df.loc[miss_idx,  num_feats + cat_feats]

    pre = ColumnTransformer(
        transformers=[
            ("num", SimpleImputer(strategy="median"), num_feats),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_feats),
        ],
        remainder="drop"
    )

    model = LinearRegression()
    pipe = Pipeline([("pre", pre), ("model", model)])
    pipe.fit(X_train, y_train)
    df.loc[miss_idx, out_col] = pipe.predict(X_test)
    return df


def is_outlier(df, column):
    # 1er Quartile 
    Q1 = df[column].quantile(0.25)
    
    # 3ème Quartile 
    Q3 = df[column].quantile(0.75)
    
    # Inter-Quartile Range (IQR)
    IQR = Q3 - Q1
    
    # limites, basse & haute
    limite_inf = Q1 - 1.5 * IQR
    limite_sup = Q3 + 1.5 * IQR
    
    # Remplace les données inférieur et supérieur à la limite par 1 et les autres par 0
    series = ((df[column] < limite_inf) | (df[column] > limite_sup)).astype(int)
    
    return series



def missing_summary(df):
    # Nombre de valeurs manquantes
    nb_missing = df.isnull().sum()
    
    # Taux de valeurs manquantes en %
    taux_missing = (df.isnull().sum() / len(df)) * 100
    
    # Regrouper dans un DataFrame
    missing_df = pd.DataFrame({
        'Nb_valeurs_manquantes': nb_missing,
        'Taux_valeurs_manquantes (%)': taux_missing
    })
    
    # Trier par ordre décroissant
    missing_df = missing_df[missing_df['Nb_valeurs_manquantes'] > 0] \
                           .sort_values(by='Nb_valeurs_manquantes', ascending=False)
    
    return missing_df

# Application
missing_summary(df)