def getGrid(Grid):

        Data = {    'A' : [[1.42, 9.08, 1.42], 
                   [9.08, 57.91, 9.08], 
                   [1.42, 9.08, 1.42]],
                'B' : [[0.15, 1.78, 1.78, 0.15],  
                   [1.78, 21.28, 21.28, 1.78], 
                   [1.78, 21.28, 21.28, 1.78],  
                   [0.15, 1.78, 1.78, 0.15]],
                'C' : [[0.03, 0.38, 0.88, 0.38, 0.03],  
                   [0.38, 4.97, 11.59, 4.97, 0.38],  
                   [0.88, 11.59, 27.05, 11.59, 0.88],  
                   [0.38, 4.97, 11.59, 4.97, 0.38],  
                   [0.03, 0.38, 0.88, 0.38, 0.03]],
                'D' : [[0.01, 0.10, 0.34, 0.34, 0.10, 0.01],  
                   [0.10, 1.22, 4.19, 4.19, 1.22, 0.10],  
                   [0.34, 4.19, 14.48, 14.48, 4.19, 0.34],  
                   [0.34, 4.19, 14.48, 14.48, 4.19, 0.34],  
                   [0.10, 1.22, 4.19, 4.19, 1.22, 0.10],  
                   [0.01, 0.10, 0.34, 0.34, 0.10, 0.01]],
                'E' : [[0, 0.03, 0.14, 0.22, 0.14, 0.03, 0], 
                   [0.03, 0.35, 1.43, 2.29, 1.43, 0.35, 0.03], 
                   [0.14, 1.43, 5.85, 9.34, 5.85, 1.43, 0.14], 
                   [0.22, 2.29, 9.34, 14.91, 9.34, 2.29, 0.22], 
                   [0.14, 1.43, 5.85, 9.34, 5.85, 1.43, 0.14], 
                   [0.03, 0.35, 1.43, 2.29, 1.43, 0.35, 0.03], 
                   [0, 0.03, 0.14, 0.22, 0.14, 0.03, 0]],
                'F' : [[0, 0.01, 0.06, 0.12, 0.12, 0.06, 0.01, 0], 
                   [0.01, 0.12, 0.52, 1.08, 1.08, 0.52, 0.12, 0.01], 
                   [0.06, 0.52, 2.25, 4.67, 4.67, 2.25, 0.52, 0.06], 
                   [0.12, 1.08, 4.67, 9.70, 9.70, 4.67, 1.08, 0.12], 
                   [0.12, 1.08, 4.67, 9.70, 9.70, 4.67, 1.08, 0.12], 
                   [0.06, 0.52, 2.25, 4.67, 4.67, 2.25, 0.52, 0.06], 
                   [0.01, 0.12, 0.52, 1.08, 1.08, 0.52, 0.12, 0.01], 
                   [0, 0.01, 0.06, 0.12, 0.12, 0.06, 0.01, 0]],
                'G' : [[0, 0.0, 1, 0.03, 0.06, 0.09, 0.06, 0.03, 0.01, 0], 
                   [0.01, 0.05, 0.21, 0.50, 0.67, 0.50, 0.21, 0.05, 0.01], 
                   [0.03, 0.21, 0.90, 2.16, 2.89, 2.16, 0.90, 0.21, 0.03], 
                   [0.06, 0.50, 2.16, 5.19, 6.96, 5.19, 2.16, 0.50, 0.06], 
                   [0.09, 0.67, 2.89, 6.96, 9.32, 6.96, 2.89, 0.67, 0.09], 
                   [0.06, 0.50, 2.16, 5.19, 6.96, 5.19, 2.16, 0.50, 0.06], 
                   [0.03, 0.21, 0.90, 2.16, 2.89, 2.16, 0.90, 0.21, 0.03], 
                   [0.01, 0.05, 0.21, 0.50, 0.67, 0.50, 0.21, 0.05, 0.01], 
                   [0, 0.0, 1, 0.03, 0.06, 0.09, 0.06, 0.03, 0.01, 0]],
                'H' : [[0, 0, 0.01, 0.03, 0.06, 0.06, 0.03, 0.01, 0, 0], 
                   [0, 0.02, 0.09, 0.24, 0.38, 0.38, 0.24, 0.09, 0.02, 0], 
                   [0.01, 0.09, 0.38, 1, 1.61, 1.61, 1, 0.38, 0.09, 0.01], 
                   [0.03, 0.24, 1, 2.6, 4.19, 4.19, 2.6, 1, 0.24, 0.03], 
                   [0.06, 0.38, 1.61, 4.19, 6.76, 6.76, 4.19, 1.61, 0.38, 0.06], 
                   [0.06, 0.38, 1.61, 4.19, 6.76, 6.76, 4.19, 1.61, 0.38, 0.06], 
                   [0.03, 0.24, 1, 2.6, 4.19, 4.19, 2.6, 1, 0.24, 0.03], 
                   [0.01, 0.09, 0.38, 1, 1.61, 1.61, 1, 0.38, 0.09, 0.01], 
                   [0, 0.02, 0.09, 0.24, 0.38, 0.38, 0.24, 0.09, 0.02, 0], 
                   [0, 0, 0.01, 0.03, 0.06, 0.06, 0.03, 0.01, 0, 0]],
                'I' : [[0, 0, 0.01, 0.02, 0.04, 0.04, 0.04, 0.02, 0.01, 0], 
                   [0, 0.01, 0.04, 0.12, 0.21, 0.26, 0.21, 0.12, 0.04, 0.01, 0], 
                   [0.01, 0.04, 0.18, 0.48, 0.86, 1.06, 0.86, 0.48, 0.18, 0.04, 0.01], 
                   [0.02, 0.12, 0.48, 1.29, 2.34, 2.86, 2.34, 1.29, 0.48, 0.12, 0.02], 
                   [0.04, 0.21, 0.86, 2.34, 4.26, 5.20, 4.26, 2.34, 0.86, 0.21, 0.04], 
                   [0.04, 0.26, 1.06, 2.86, 5.20, 6.34, 5.20, 1.06, 2.86, 0.26, 0.04], 
                   [0.04, 0.21, 0.86, 2.34, 4.26, 5.20, 4.26, 2.34, 0.86, 0.21, 0.04], 
                   [0.02, 0.12, 0.48, 1.29, 2.34, 2.86, 2.34, 1.29, 0.48, 0.12, 0.02], 
                   [0.01, 0.04, 0.18, 0.48, 0.86, 1.06, 0.86, 0.48, 0.18, 0.04, 0.01], 
                   [0, 0.01, 0.04, 0.12, 0.21, 0.26, 0.21, 0.12, 0.04, 0.01, 0], 
                   [0, 0, 0.01, 0.02, 0.04, 0.04, 0.04, 0.02, 0.01, 0]],
                'J' : [[0, 0, 0, 0.01, 0.02, 0.03, 0.03, 0.02, 0.01, 0, 0, 0], 
                   [0, 0.01, 0.02, 0.06, 0.12, 0.17, 0.17, 0.12, 0.06, 0.02, 0.01, 0], 
                   [0, 0.02, 0, 0.24, 0.47, 0.65, 0.65, 0.47, 0.24, 0, 0.02, 0], 
                   [0.01, 0.06, 0.24, 0.65, 1.28, 1.79, 1.79, 1.28, 0.65, 0.24, 0.06, 0.01], 
                   [0.02, 0.12, 0.47, 1.28, 2.51, 3.52, 3.52, 2.51, 1.28, 0.47, 0.12, 0.02], 
                   [0.03, 0.17, 0.65, 1.79, 3.52, 4.93, 4.93, 3.52, 1.79, 0.65, 0.17, 0.03], 
                   [0.03, 0.17, 0.65, 1.79, 3.52, 4.93, 4.93, 3.52, 1.79, 0.65, 0.17, 0.03], 
                   [0.02, 0.12, 0.47, 1.28, 2.51, 3.52, 3.52, 2.51, 1.28, 0.47, 0.12, 0.02], 
                   [0.01, 0.06, 0.24, 0.65, 1.28, 1.79, 1.79, 1.28, 0.65, 0.24, 0.06, 0.01], 
                   [0, 0.02, 0, 0.24, 0.47, 0.65, 0.65, 0.47, 0.24, 0, 0.02, 0], 
                   [0, 0.01, 0.02, 0.06, 0.12, 0.17, 0.17, 0.12, 0.06, 0.02, 0.01, 0], 
                   [0, 0, 0, 0.01, 0.02, 0.03, 0.03, 0.02, 0.01, 0, 0, 0]] }
    
        return Data[Grid]
        
