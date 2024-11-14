from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")
def MeuSalario():
    return render_template("MeuSalario.html")


@app.route("/resultado", methods=['POST', 'GET'])
def resultado():

#Capturando Valores<<

    referencia = request.form.get('referencia')
    num_plantao = request.form.get('num_plantao')
    num_extra24 = request.form.get('num_extra24')
    var_extra24 = 487.03
    num_extra10dia = request.form.get('num_extra10dia')
    var_extra10dia = 174.49
    num_extra10noite = request.form.get('num_extra10noite')
    var_extra10noite = 214.26
    var_extraExtraordinaria = request.form.get('ex_exepcionais_valor')
    num_extraExtraordinaria = request.form.get('ex_exepcionais_quantidade')
    gra_patrulhas = request.form.get('funcao')
    cargo=request.form.get('cargos')
    quiquenio = request.form.get('vol')
    sindicato = request.form.get('sindicato')
    
# Convertendo os valores
# Valores Base<<
    if referencia == "I":
        con_base = 1800.00
        referencia = "I / Probatorio"
    elif referencia == "II":
        con_base = 1908.00
        referencia = "II / 5 Anos"
    elif referencia == "III":
        con_base = 1984.32
        referencia = "III / 7 Anos"
    elif referencia == "IV":
        con_base = 2063.69
        referencia = "IV / 9 Anos"
    elif referencia == "V":
        con_base = 2146.24
        referencia = "V / 11 Anos"
    elif referencia == "VI":
        con_base = 2232.09
        referencia = "VI / 13 Anos"
    elif referencia == "VII":
        con_base = 2678.51
        referencia = "VII / 15 Anos"
    elif referencia == "VIII":
        con_base = 2785.65
        referencia = "VIII / 17 Anos"
    elif referencia == "IX":
        con_base = 2897.07
        referencia = "IX / 19 Anos"
    elif referencia == "X":
        con_base = 3012.96
        referencia = "X / 21 Anos"
    elif referencia == "XI":
        con_base = 3073.22
        referencia = "XI / 23 Anos"
    elif referencia == "XII":
        con_base = 4073.46
        referencia = "XII / 25 Anos"
    elif referencia == "XIII":
        con_base = 4236.39
        referencia = "XIII / 27 Anos"
    elif referencia == "XIV":
        con_base = 4405.85
        referencia = "XIV / 29 Anos"
    elif referencia == "XV":
        con_base = 4670.20
        referencia = "XV / 31 Anos"
    elif referencia == "XVI":
        con_base = 4950.41
        referencia = "XVI / 33 Anos"
    else:
        con_base = 0
        referencia = "Classe e Referencia erradas"

    
    con_baseInicial= 1800 #Valor Base inicial
    con_num_plantao = int(num_plantao) # Numero de plantões
    con_num_extra24 = int(num_extra24) # Numero de Extra 24 horas
    con_var_extra24 = float(var_extra24) # Valores da Extra 24 horas
    con_num_extra10dia = int(num_extra10dia)# Numero de Extra 10 horas dias
    con_var_extra10dia = float(var_extra10dia)# Valores da Extra 10 horas dia
    con_num_extra10noite = int(num_extra10noite)# Numero de Extra 10 horas noite
    con_var_extra10noite = float(var_extra10noite)# Valores da Extra 10 horas noite
    con_gra_patrulhas = float(gra_patrulhas) # Porcentagem da gratificação de patrulha
    con_quiquenio = int(quiquenio) # Numeor de quiquenio
    con_var_extraExepicao = float(var_extraExtraordinaria)
    con_num_extraExtraordinaria = int(num_extraExtraordinaria)
    cargo = float(cargo)

     #>>>Calculos<<<

    
    horas = con_num_plantao * 24 # Totla de Horas trabalhadas
    if con_num_plantao == 8:
        horas_extras = (con_num_extra10dia + con_num_extra10noite *
                        10) + (con_num_extra24 * 24) + 32
    else:
        horas_extras = (con_num_extra10dia +
                        con_num_extra10noite * 10) + (con_num_extra24 * 24) + 8


    # Risco
    risco = con_base * 0.35

    # Alimentação
    ticket = con_baseInicial * 0.02
    alimentacao = round((ticket * con_num_plantao * 3) + (con_num_extra24 * ticket * 3) + (
        con_num_extra10dia * ticket * 1) + (con_num_extra10noite * ticket * 1), 2)

    # Valores das extras
    extra24 = con_var_extra24 - (ticket * 3)
    if con_var_extra10dia > 0:
        extra10d = con_var_extra10dia - (ticket * 1)
    else:
        extra10d = 0
    if con_var_extra10noite > 0:
        extra10n = con_var_extra10noite - (ticket * 1)
    else:
        extra10n = 0

    total_extra24 = round(extra24 * con_num_extra24, 2)
    total_extra10 = round((extra10d * con_num_extra10dia) +
                          (extra10n * con_num_extra10noite), 2)

    # Extra Extraordinaria
    extra_extraordianria = round(
        con_var_extraExepicao * con_num_extraExtraordinaria, 2)

    # Hora extras
    if con_num_plantao == 8:# Calculo das horas Extras 8 plantão
        hora_extra50 = round((con_base / 160) * 1.50 * 17, 2)# Calculo das horas Extras 50% 8 plantão
        hora_extra75 = round((con_base / 160) * 1.75 * 15, 2)# Calculo das horas Extras 75% 8 plantão
    elif con_num_plantao == 7:# Calculo das horas Extras 7 plantão
        hora_extra50 = round((con_base / 160) * 1.50 * 4, 2)# Calculo das horas Extras 50% 7 plantão
        hora_extra75 = round((con_base / 160) * 1.75 * 4, 2)# Calculo das horas Extras 75% 7 plantão
    else:# mensagem de erro
        hora_extra50 = 'Numero de plantão invalido'
        hora_extra75 = 'Numero de plantão invalido'

    # Gratificações de patrulhas
    gratificacao_patrulha = con_base * (con_gra_patrulhas/100)

    # Quiquenio
    val_quiquenio = con_base * 0.05 * con_quiquenio

    # Adicional noturno
    if con_num_plantao == 8:
        adicional_noturno = round((con_base / 160) * 0.20 * 64, 2)
    elif con_num_plantao == 7:
        adicional_noturno = round((con_base / 160) * 0.20 * 56, 2)
    else:
        adicional_noturno = 'Revise os valores fornecidos'

    # Descontos Santa Cruz PREV
    if con_num_plantao == 7 or con_num_plantao == 8:
        preve = round(con_base * 0.14, 2)
    else:
        preve = 'Revise os valores fornecidos'

    # Sindicato
    if sindicato == "sim":
        des_sindicato = con_base * 0.02
    else:
        des_sindicato = 0

    # Cargos
    if cargo == 50:
        cargos = con_baseInicial * 0.5
    elif cargo == 85:
        cargos = con_baseInicial * 0.85
    else:
        cargos = 0
        

    # Imposto de renda
    if con_num_plantao == 8 or con_num_plantao == 7: # Base de Calculo
        IRF = con_base + risco + hora_extra50 + hora_extra75 + \
            total_extra24 + total_extra10 + adicional_noturno + val_quiquenio + \
            extra_extraordianria + gratificacao_patrulha - preve 

        if 0 <= IRF <= 2259.20:
            imposto = 0
            faixa = 'Insento'
        elif 2259.21 <= IRF <= 2828.65:
            imposto = round((IRF * 0.0750) - 169.44, 2)
            faixa = '7,50%'
        elif 2828.66 <= IRF <= 3751.05:
            imposto = round((IRF * 0.150) - 381.44, 2)
            faixa = '15%'
        elif 3751.06 <= IRF <= 4664.68:
            imposto = round((IRF * 0.2250) - 662.77, 2)
            faixa = '22,50%'
        else:
            imposto = round((IRF * 0.270) - 896.00, 2)
            faixa = '27%'
    else:
        IRF = "erro"
        imposto = 'Revise os valores fornecidos'
        faixa = 'Revise os valores fornecidos'

    # Salario
    if con_num_plantao == 7 or con_num_plantao == 8:
        bruto = round(con_base + risco + alimentacao + total_extra24 +
                      total_extra10 + hora_extra50 + hora_extra75 + adicional_noturno + val_quiquenio + gratificacao_patrulha + extra_extraordianria, 2)
    else:
        bruto = 'Revise os valores fornecidos'

    if con_num_plantao == 7 or con_num_plantao == 8:
        liquido = round(con_base + risco + alimentacao + adicional_noturno + total_extra24 +
                        total_extra10 + hora_extra50 + hora_extra75 + val_quiquenio + gratificacao_patrulha - preve - imposto - des_sindicato, 2)
    else:
        liquido = 'Revise os valores fornecidos'

    # Formatando os valores
    con_base = "{:.2f}".format(con_base).replace(".", ",")
    risco = "{:.2f}".format(risco).replace(".", ",")
    alimentacao = "{:.2f}".format(alimentacao).replace(".", ",")
    hora_extra50 = "{:.2f}".format(hora_extra50).replace(".", ",")
    hora_extra75 = "{:.2f}".format(hora_extra75).replace(".", ",")
    adicional_noturno = "{:.2f}".format(adicional_noturno).replace(".", ",")
    total_extra24 = "{:.2f}".format(total_extra24).replace(".", ",")
    total_extra10 = "{:.2f}".format(total_extra10).replace(".", ",")
    preve = "{:.2f}".format(preve).replace(".", ",")
    imposto = "{:.2f}".format(imposto).replace(".", ",")
    bruto = "{:.2f}".format(bruto).replace(".", ",")
    liquido = "{:.2f}".format(liquido).replace(".", ",")
    des_sindicato = "{:.2f}".format(des_sindicato).replace(".", ",")
    val_quiquenio = "{:.2f}".format(val_quiquenio).replace(".", ",")
    gratificacao_patrulha = "{:.2f}".format(
        gratificacao_patrulha).replace(".", ",")
    extra_extraordianria = "{:.2f}".format(
        extra_extraordianria).replace(".", ",")
    cargos = "{:.2f}".format(cargos).replace(".",",")

    # Apresentando valores
    print('O valor é de {} e tem o tipo de {} e o valor calculado e de {}'.format(cargo, type(cargo), cargos))
    return render_template('resultado.html',
                           referencia=referencia,
                           base=con_base,
                           platao=num_plantao,
                           risco=risco,
                           hora_extra50=hora_extra50,
                           hora_extra75=hora_extra75,
                           alimentacao=alimentacao,
                           extra24=total_extra24,
                           extra10=total_extra10,
                           extraordinaria=extra_extraordianria,
                           preve=preve,
                           imposto=imposto,
                           bruto=bruto,
                           liquido=liquido,
                           adicional_noturno=adicional_noturno,
                           faixa=faixa,
                           des_sindicato=des_sindicato,
                           horas=horas,
                           horas_extras=horas_extras,
                           val_quiquenio=val_quiquenio,
                           gratificacao_patrulha=gratificacao_patrulha,
                           cargos=cargos
                           )


if __name__ == "__main__":
    app.run(debug=True)
