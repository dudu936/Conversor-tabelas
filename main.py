pdf_file = "RELATORIO-18-05-2023.pdf"
xlsx_file = pdf_file[:-3] + "xlsx"
rows=["C.Pagar: Nr. Lanc.","COMPRA MERCADORIA","Dt. Entrada","dias","Código Conta","Prazo Indice"]
separator=["Embalagem UN Qt. P.Unit. Custo Fin.Ant.","Filial Embalagem UN Qt.","UN Qt. P.Unit. Custo Fin.Ant.","Filial Embalagem UN","Embalagem UN Qt.","UN Qt. P.Unit.","Qt. P.Unit. Custo Fin.Ant.","P.Unit. Custo Fin.Ant. Custo Fin.Atual","Custo Fin.Ant. Custo Fin.Atual Cód. Fiscal","Custo Fin.Atual Cód. Fiscal Cód. Oper.","Filial Embalagem","Embalagem UN","UN Qt.","Qt. P.Unit. Custo","P.Unit. Custo Fin.Ant.","Custo Fin.Ant. Custo Fin.Atual","Custo Fin.Atual Cód. Fiscal","Cód. Fiscal Cód. Oper."]
columns=["Filial","Embalagem","Custo Fin.Atual","Custo","Fin.Ant.","Fin.Atual","Cód. Fiscal","Cód.","Fiscal","Cód. Oper.","NaN","nan"]

main(pdf_file=pdf_file,xlsx_file=xlsx_file,index=1,rows=rows,columns=columns,separator=separator)
