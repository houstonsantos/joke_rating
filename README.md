<div align="center">

![hou](https://datahack-prod.s3.ap-south-1.amazonaws.com/__sized__/contest_cover/is_this_funny-thumbnail-1200x1200-70.jpg)

</div>

Nesta competição da Analytics Vidhya temos que prever notas que são atribuidas a piadas, vamos cria um modelo de recomendação (**RecSys**). Para validarmos o modelo vou utilizar a métrica **RMSE** estipulada pela competição.

<p align="center">
    <img width="700" height="250" src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*kgBD8OuP7SMsL63gcsQ90Q.png">
</p>

Os exemplos são diversos: a Amazon recomenda livros (ou qual coisa do marketplace), a Netflix faz recomendação de Filmes, o Mendeley recomenda artigos ciêntíficos, a Globo.com recomenda notícias e o Spotify às músicas.

*   Temos algumas opções de algoritimos de Machine Learning para RecSys.

    *   Filtragem Baseada em Conteúdo (Content-Based)
    *   Filtragem Colaborativa (Collaborative Filter)
    *   Sistemas Híbridos (Hybrid)
    *   Cold-Start

### Approach

Utilizando à biblioteca [_**Surprise**_](https://surpriselib.com/), irei cria um modelos utilizando **SVD** _(Singular Value Decomposition)_, _Filtragem Colaborativa_.

O **SVD** realiza a fatoração de matrizes, isso pode ser um problema quando temos muitos dados, pois às matrizes seram muito esparsas, isso resultarar em custo computacional muito alto levando muito tempo de processamento. Mas vamos em frente....

$$
\begin{align} 
\hat r_i = \mu + b_u + b_i + q_i^T p_u
\end{align}
$$