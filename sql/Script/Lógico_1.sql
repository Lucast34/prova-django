/* Lógico_1: */

CREATE TABLE tb_palavra (
    id INT PRIMARY KEY,
    palavra VARCHAR
);

CREATE TABLE tb_regra (
    id INT PRIMARY KEY,
    tipo_uso VARCHAR,
    tipo_escrita VARCHAR,
    tipo_paronimos VARCHAR,
    tipo_homonimos VARCHAR,
    fk_tb_categoria_id INT
);

CREATE TABLE tb_categoria (
    id INT PRIMARY KEY,
    tipo_exececoes VARCHAR
);

CREATE TABLE tb_palavra_regra (
    id INT PRIMARY KEY,
    fk_tb_regra_id INT,
    fk_tb_palavra_id INT
);
 
ALTER TABLE tb_regra ADD CONSTRAINT FK_tb_regra_2
    FOREIGN KEY (fk_tb_categoria_id)
    REFERENCES tb_categoria (id)
    ON DELETE RESTRICT;
 
ALTER TABLE tb_palavra_regra ADD CONSTRAINT FK_tb_palavra_regra_2
    FOREIGN KEY (fk_tb_regra_id)
    REFERENCES tb_regra (id)
    ON DELETE RESTRICT;
 
ALTER TABLE tb_palavra_regra ADD CONSTRAINT FK_tb_palavra_regra_3
    FOREIGN KEY (fk_tb_palavra_id)
    REFERENCES tb_palavra (id)
    ON DELETE RESTRICT;