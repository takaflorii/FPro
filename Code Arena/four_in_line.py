def four_in_line(board):
    falinks = len(board) #Falinks (Pokemon composto por 4 cabeças em linha) é o número de linhas do tabuleiro
    if falinks == 0:
        return ()
    sentret = len(board[0]) #Sentret (Pokemon que se coloca na vertical) é o número de colunas do tabuleiro

    direcoes = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    for linha in range(falinks):
        for coluna in range(sentret):
            a_que_jogador_pertence = board[linha][coluna]
            if a_que_jogador_pertence == 0:
                continue
                
            for dl, dc in direcoes:
                l_final = linha + 3 * dl
                c_final = coluna + 3 * dc
                
                if 0 <= l_final < falinks and 0 <= c_final < sentret:
                    if all(board[linha + i * dl][coluna + i * dc] == a_que_jogador_pertence for i in range(4)):
                        comeco = (linha, coluna)
                        final = (l_final, c_final)
                        
                        if comeco > final:
                            comeco, final = final, comeco
                            
                        return (comeco, final)
                        
    return ()
