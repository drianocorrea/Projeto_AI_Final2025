from listPath import listPath


class searchPath(object):

    # SUCESSORES PARA GRAFO (LISTA DE ADJACENCIAS)
    def sucessores(self, ind, grafo, ordem):
        f = []
        if ind < len(grafo):
            for suc in grafo[ind][::ordem]:
                if suc:  # verifica se não é vazio
                    f.append(suc)
        return f
# ------------------------------------------------------------------------------
    # CONTROLE DE NÓS REPETIDOS

    def verificaVisitado(self, novo, nivel, visitado):
        flag = True
        # controle de nós repetidos
        for aux in visitado:
            if aux[0] == novo:
                if aux[1] <= (nivel+1):
                    flag = False
                else:
                    aux[1] = nivel+1
                break
        return flag
    # ---------------------------------------------
    # BUSCA EM AMPLITUDE

    def amplitude(self, inicio, fim, nos, grafo):

        # manipular a FILA para a busca
        l1 = listPath()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listPath()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()

            ind = nos.index(atual.estado)
            filhos = self.sucessores(ind, grafo, 1)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                # verifica se foi visitado
                flag = self.verificaVisitado(novo, atual.v1, visitado)

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.v1+1, 0, atual)
                    l2.insereUltimo(novo, atual.v1+1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.v1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        # print("\nFila:\n",l1.exibeLista())
                        # print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return None
    # ---------------------------------------------
    # BUSCA EM PROFUNDIDADE

    def profundidade(self, inicio, fim, nos, grafo):
        # manipular a PILHA para a busca
        l1 = listPath()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listPath()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o último da PILHA
            atual = l1.deletaUltimo()

            ind = nos.index(atual.estado)
            filhos = self.sucessores(ind, grafo, 1)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                # verifica se foi visitado
                flag = self.verificaVisitado(novo, atual.v1, visitado)

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.v1+1, 0, atual)
                    l2.insereUltimo(novo, atual.v1+1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.v1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        # print("\nFila:\n",l1.exibeLista())
                        # print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return None
    # ---------------------------------------------
    # BUSCA EM PROFUNDIDADE LIMITADA

    def proflimitada(self, inicio, fim, nos, grafo, lim=5):
        # manipular a PILHA para a busca
        l1 = listPath()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listPath()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o último da PILHA
            atual = l1.deletaUltimo()

            if atual.v1 < lim:
                ind = nos.index(atual.estado)
                filhos = self.sucessores(ind, grafo, 1)

                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:

                    # verifica se foi visitado
                    flag = self.verificaVisitado(novo, atual.v1, visitado)

                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.v1+1, 0, atual)
                        l2.insereUltimo(novo, atual.v1+1, 0, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado.append(linha)

                        # verifica se é o objetivo
                        if novo == fim:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            # print("\nFila:\n",l1.exibeLista())
                            # print("\nÁrvore de busca:\n",l2.exibeLista())
                            return caminho

        return None
    # ---------------------------------------------
    # BUSCA EM APROFUNDAMENTO ITERATIVO

    def aprof_iterativo(self, inicio, fim, nos, grafo, l_max):
        for lim in range(1, l_max):
            # manipular a PILHA para a busca
            l1 = listPath()

            # cópia para apresentar o caminho (somente inserção)
            l2 = listPath()

            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio, 0, 0, None)
            l2.insereUltimo(inicio, 0, 0, None)

            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)

            while l1.vazio() == False:
                # remove o último da PILHA
                atual = l1.deletaUltimo()

                if atual.v1 < lim:
                    ind = nos.index(atual.estado)
                    filhos = self.sucessores(ind, grafo, 1)

                    # varre todos as conexões dentro do grafo a partir de atual
                    for novo in filhos:

                        # verifica se foi visitado
                        flag = self.verificaVisitado(novo, atual.v1, visitado)

                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.v1+1, 0, atual)
                            l2.insereUltimo(novo, atual.v1+1, 0, atual)

                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.v1+1)
                            visitado.append(linha)

                            # verifica se é o objetivo
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                # print("\nFila:\n",l1.exibeLista())
                                # print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho

        return None
    # ----------------------------------------------------  # BUSCA BIDIRECIONAL

    def bidirecional(self, inicio, fim, nos, grafo):
        # Primeiro Amplitude"
        # Manipular a FILA para a busca
        l1 = listPath()
        # cópia para apresentar o caminho (somente inserção)
        l2 = listPath()

        # Segundo Amplitude"
        # Manipular a FILA para a busca
        l3 = listPath()
        # cópia para apresentar o caminho (somente inserção)
        l4 = listPath()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        l3.insereUltimo(fim, 0, 0, None)
        l4.insereUltimo(fim, 0, 0, None)

        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)

        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)

        ni = 0
        while l1.vazio() == False or l3.vazio() == False:

            while l1.vazio() == False:

                # para ir para o próximo amplitude
                if ni != l1.primeiro().v1:
                    break

                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()

                ind = nos.index(atual.estado)
                filhos = self.sucessores(ind, grafo, 1)

                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:

                    # pressuponho que não foi visitado
                    flag = self.verificaVisitado(novo, atual.v1+1, visitado1)
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.v1+1, 0, atual)
                        l2.insereUltimo(novo, atual.v1+1, 0, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado1.append(linha)

                        # verifica se é o objetivo
                        flag = not (self.verificaVisitado(
                            novo, atual.v1+1, visitado2))
                        if flag:
                            caminho = []
                            # print("Fila:\n",l1.exibeLista())
                            # print("\nÁrvore de busca:\n",l2.exibeLista())
                            # print("\nÁrvore de busca:\n",l4.exibeLista())
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho

            while l3.vazio() == False:

                # para ir para o próximo amplitude
                if ni != l3.primeiro().v1:
                    break

                # remove o primeiro da fila
                atual = l3.deletaPrimeiro()

                ind = nos.index(atual.estado)
                filhos = self.sucessores(ind, grafo, 1)

                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:

                    # pressuponho que não foi visitado
                    flag = self.verificaVisitado(novo, atual.v1+1, visitado2)
                    # se não foi visitado inclui na fila
                    if flag:
                        l3.insereUltimo(novo, atual.v1+1, 0, atual)
                        l4.insereUltimo(novo, atual.v1+1, 0, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado2.append(linha)

                        # verifica se é o objetivo
                        flag = not (self.verificaVisitado(
                            novo, atual.v1+1, visitado1))
                        if flag:
                            caminho = []
                            # print("Fila:\n",l3.exibeLista())
                            # print("\nÁrvore de busca:\n",l4.exibeLista())
                            # print("\nÁrvore de busca:\n",l2.exibeLista())
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]

            ni += 1

        return "caminho não encontrado"

    # ---------------------------------------------
    # BUSCA DE CUSTO UNIFORME

    def custo_uniforme(self, inicio, fim, nos, grafo):
        l1 = listPath()  # Lista ordenada por custo
        l2 = listPath()  # Árvore de busca

        # Inserir nó inicial
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        # Conjunto de nós visitados com seus custos
        visitados = {}

        while not l1.vazio():
            atual = l1.deletaPrimeiro()

            if atual.estado == fim:
                return l2.exibeCaminho()

            if atual.estado in visitados and visitados[atual.estado] <= atual.v1:
                continue

            visitados[atual.estado] = atual.v1

            # Explorar sucessores
            ind = nos.index(atual.estado)
            for cidade in grafo[ind][1:]:
                if cidade:  # verifica se não é vazio
                    novo_custo = atual.v1 + 1  # Custo uniforme para cada passo
                    if cidade not in visitados or novo_custo < visitados[cidade]:
                        l1.insereUltimo(cidade, novo_custo, 0, atual)
                        l2.insereUltimo(cidade, novo_custo, 0, atual)

        return None

    # ---------------------------------------------
    # BUSCA GULOSA (GREEDY)

    def greedy(self, inicio, fim, nos, grafo, heuristica):
        l1 = listPath()  # Ordenado pela heurística
        l2 = listPath()  # Árvore de busca

        # Garante que o nó inicial tem uma heurística
        h_inicio = heuristica.get(inicio, float('inf'))
        l1.insereUltimo(inicio, 0, h_inicio, None)
        l2.insereUltimo(inicio, 0, h_inicio, None)

        visitados = []

        while not l1.vazio():
            atual = l1.deletaPrimeiro()

            if atual.estado == fim:
                caminho = l2.exibeCaminho()
                return caminho

            if atual.estado in visitados:
                continue

            visitados.append(atual.estado)

            ind = nos.index(atual.estado)
            for conexao in grafo[ind][1:]:
                if conexao and conexao not in visitados:
                    h = heuristica.get(conexao, float('inf'))
                    l1.insereUltimo(conexao, 0, h, atual)
                    l2.insereUltimo(conexao, 0, h, atual)

        return None

    # ---------------------------------------------
    # BUSCA A*

    def a_estrela(self, inicio, fim, nos, grafo, heuristica):
        l1 = listPath()  # Ordenado por f(n) = g(n) + h(n)
        l2 = listPath()  # Árvore de busca

        # Garante que o nó inicial tem uma heurística
        h_inicio = heuristica.get(inicio, float('inf'))
        l1.insereUltimo(inicio, 0, h_inicio, None)
        l2.insereUltimo(inicio, 0, h_inicio, None)

        visitados = {}

        while not l1.vazio():
            atual = l1.deletaPrimeiro()

            if atual.estado == fim:
                caminho = l2.exibeCaminho()
                return caminho

            if atual.estado in visitados and visitados[atual.estado] <= atual.v1:
                continue

            visitados[atual.estado] = atual.v1

            ind = nos.index(atual.estado)
            for conexao in grafo[ind][1:]:
                if conexao:  # verifica se não é vazio
                    g_novo = atual.v1 + 1
                    h_novo = heuristica.get(conexao, float('inf'))
                    f_novo = g_novo + h_novo

                    if conexao not in visitados or g_novo < visitados[conexao]:
                        l1.insereUltimo(conexao, g_novo, f_novo, atual)
                        l2.insereUltimo(conexao, g_novo, f_novo, atual)

        return None

    # ---------------------------------------------
    # BUSCA A* ITERATIVO (IDA*)

    def aia_estrela(self, inicio, fim, nos, grafo, heuristica, l_max):
        for limite in range(1, l_max + 1):
            resultado = self._a_estrela_limitado(inicio, fim, nos, grafo, heuristica, limite)
            if resultado:
                return resultado
        return None

    def _a_estrela_limitado(self, inicio, fim, nos, grafo, heuristica, limite):
        l1 = listPath()
        l2 = listPath()

        # Garante que o nó inicial tem uma heurística
        h_inicio = heuristica.get(inicio, float('inf'))
        l1.insereUltimo(inicio, 0, h_inicio, None)
        l2.insereUltimo(inicio, 0, h_inicio, None)

        visitados = {}

        while not l1.vazio():
            atual = l1.deletaPrimeiro()

            if atual.estado == fim:
                caminho = l2.exibeCaminho()
                return caminho

            if atual.v1 + atual.v2 > limite:
                continue

            if atual.estado in visitados and visitados[atual.estado] <= atual.v1:
                continue

            visitados[atual.estado] = atual.v1

            ind = nos.index(atual.estado)
            for conexao in grafo[ind][1:]:
                if conexao:  # verifica se não é vazio
                    g_novo = atual.v1 + 1
                    h_novo = heuristica.get(conexao, float('inf'))
                    f_novo = g_novo + h_novo

                    if f_novo <= limite and (conexao not in visitados or g_novo < visitados[conexao]):
                        l1.insereUltimo(conexao, g_novo, f_novo, atual)
                        l2.insereUltimo(conexao, g_novo, f_novo, atual)

        return None
