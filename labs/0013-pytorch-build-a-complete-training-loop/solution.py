import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

def train_model(model, X_train, y_train, X_val, y_val, epochs, batch_size, lr):
    # TODO: Implement the training loop
    
    history = []

    #Mini-Batching...Code---For
    def make_batches(X,y):
        n_samples = X.shape[0] 
        perm = torch.randperm(X.shape[0])
        X_shuffled = X[perm]
        y_shuffled = y[perm]
        n_batches = (X_train.shape[0]+batch_size-1)//batch_size
        batches = []
        for i in range(n_batches):
            start = i * n_batches
            end = min(start+batch_size,n_samples)
            batches.append((X_shuffled[start:end],y_shuffled[start:end]))
        return batches
    
    #Dataset Preperation
    train_batches = make_batches(X_train,y_train)
    val_batches = make_batches(X_val,y_val)
    
    optimizer = torch.optim.Adam(model.parameters(),lr=lr)
    criterion = nn.CrossEntropyLoss()
    #Tranning Loop----->
    for epoch in range(epochs):
        model.train()
        running_train_loss = 0
        for idx, batch in enumerate(train_batches):
            x_batch, y_batch = batch
            optimizer.zero_grad()
            output = model(x_batch)
            loss = criterion(output,y_batch)
            loss.backward()
            optimizer.step()

            running_train_loss += loss.item()
        
        model.eval()
        running_val_loss=0
        with torch.no_grad():
            for x_val_batch, y_val_batch in val_batches:
                val_output = model(x_val_batch)
                val_pred = val_output.argmax(dim=1)
                val_accuracy = (val_pred == y_val_batch).float().mean().item()
                loss = criterion(val_output,y_val_batch)
                running_val_loss += loss.item()
        
        epoch_train_loss = running_train_loss/len(train_batches)
        epoch_val_loss = running_val_loss/len(val_batches)
        # print(f"Epoch [{epoch+1}/{epochs}] -> Train Loss {epoch_train_loss:.4f} | Val Loss: {epoch_val_loss:.4f}")


        
    
        history.append({'epoch': epoch+1,
                        'train_loss':epoch_train_loss,
                        'val_loss':epoch_val_loss,
                        'val_accuracy': val_accuracy
                        })
    
    return history
