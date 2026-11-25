"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    # Prompt sugerido: "Crie um histograma da coluna rating com 20 bins, título e
    #  labels em português, e salve a figura em out_path."
    df = df.copy()
    plt.figure(figsize=(10, 6))
    sns.histplot(df['rating'], bins=20, kde=False)
    plt.title('Distribuição de Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequência')
    plt.savefig(out_path)
    plt.close()
    # raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    df = df.copy()
    top_varieties = df['variety'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_varieties.values, y=top_varieties.index)
    plt.title('Top 10 Variedades de Vinhos')
    plt.xlabel('Quantidade de Vinhos')
    plt.ylabel('Variedade')
    plt.savefig(out_path)
    plt.close()
    # raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Salve a figura
    em ``out_path``."""
    df = df.copy()
    top_varieties = df['variety'].value_counts().head(5).index
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='variety', y='rating', data=df[df['variety'].isin(top_varieties)])
    plt.title('Boxplot de Ratings por Variedade (Top 5)')
    plt.xlabel('Variedade')
    plt.ylabel('Rating')
    plt.savefig(out_path)
    plt.close()
    # raise NotImplementedError("Implemente com o apoio do GitHub Copilot.")
