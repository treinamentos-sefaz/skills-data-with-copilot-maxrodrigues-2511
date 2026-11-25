"""Módulo 2 — Manipulação de DataFrames com pandas.

Complete cada função com o apoio do GitHub Copilot. Prefira operações
vetorizadas e evite alterar o DataFrame original (use ``.copy()``).

Valide com:  ``python lab/check.py --module pandas``
"""
from __future__ import annotations

import pandas as pd


def load_wines(path: str) -> pd.DataFrame:
    """Leia o CSV em ``path`` e retorne um DataFrame do pandas."""
    # Prompt sugerido: "Leia o arquivo CSV em path com pandas e retorne o DataFrame."
    return pd.read_csv(path)
    # raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Converta a coluna ``rating`` para numérico e remova as linhas cujo
    ``rating`` seja nulo. Retorne o DataFrame limpo."""
    df = df.copy()
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df = df.dropna(subset=['rating'])
    return df
    # raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def top_varieties_by_avg_rating(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Retorne as ``n`` variedades com maior média de ``rating`` (colunas:
    variety, avg_rating), ordenadas da maior para a menor."""
    df = df.copy()
    result = df.groupby('variety')['rating'].mean().reset_index()
    result = result.rename(columns={'rating': 'avg_rating'})
    result = result.sort_values(by='avg_rating', ascending=False).head(n)
    return result
    # raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def add_rating_category(df: pd.DataFrame) -> pd.DataFrame:
    """Adicione a coluna ``rating_category`` com as faixas: "Baixa" (< 85),
    "Média" (85 a 90) e "Alta" (> 90). Dica: use ``pd.cut``."""
    df = df.copy()
    bins = [float('-inf'), 85, 90, float('inf')]
    labels = ['Baixa', 'Média', 'Alta']
    df['rating_category'] = pd.cut(df['rating'], bins=bins, labels=labels)
    return df
    # raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def enrich_with_country(df: pd.DataFrame) -> pd.DataFrame:
    """Adicione a coluna ``country`` extraindo o último trecho após a vírgula de
    ``region`` (ex.: "Mendocino, California" -> "California")."""
    df = df.copy()
    df['country'] = df['region'].str.split(',').str[-1].str.strip()
    return df
    # raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")
