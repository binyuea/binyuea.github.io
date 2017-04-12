mutex bathroom_lock;
cv men, women;
int active_men = 0;
int active_women = 0;

woman_wants_to_enter(){
	bathroom_lock.lock();
	while(active_men){
		women.wait();
	}
	active_women++;
	bathroom_lock.unlock();
}

woman_leaves(){
	bathroom_lock.lock();
	active_women--;
	if(active_women == 0){
		men.broadcast();
	}
	bathroom_lock.unlock();
}