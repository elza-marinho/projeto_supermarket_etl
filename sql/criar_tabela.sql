CREATE DATABASE supermarket;

CREATE TABLE public.raw_venda (
    id_venda varchar(10) NULL,
    filial varchar(100) NULL,
    cidade varchar(100) NULL,
    tipo_cliente varchar(50) NULL,
    genero varchar(10) NULL,
    linha_produto varchar(150) NULL,
    preco_unitario varchar(20) NULL,
    quantidade varchar(10) NULL,
    imposto varchar(20) NULL,
    valor_total varchar(30) NULL,
    data_venda varchar(30) NULL,
    hora_venda varchar(30) NULL,
    forma_pagamento varchar(25) NULL,
    custo_produto varchar(15) NULL,
    margem_percentual varchar(20) NULL,
    avaliacao varchar(10) NULL
);

CREATE TABLE public.venda_tratada (
    id_venda varchar(10) NOT NULL,
    filial varchar(50) NOT NULL,
    cidade varchar(100) NOT NULL,
    tipo_cliente varchar(25) NOT NULL,
    genero varchar(10) NULL CHECK (genero IN ('Male','Female')),
    linha_produto varchar(150) NOT NULL,
    preco_unitario NUMERIC(10, 2) NOT NULL  CHECK (preco_unitario >= 0),
    quantidade INT NOT NUL CHECK (quantidade > 0),
    imposto NUMERIC(10, 2) NULL CHECK (imposto >= 0),
    valor_total NUMERIC(10, 2) NULL CHECK (valor_total >= 0),
    data_venda date NOT NULL,
    hora_venda time NOT NULL,
    forma_pagamento varchar(50) NOT NULL,
    custo_produto NUMERIC(10, 2) NOT NULL CHECK (custo_produto >= 0),
    margem_percentual NUMERIC(10, 2) NULL,
    receita_bruta NUMERIC(10, 2) NULL CHECK (receita_bruta >= 0),
    avaliacao NUMERIC(3, 1) NULL CHECK (avaliacao BETWEEN 0 AND 10),

);
