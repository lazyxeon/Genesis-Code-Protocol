use glam::Vec3;

#[derive(Debug)]
pub struct Stats {
    pub health: f32,
    pub mana: f32,
    pub level: u32,
    pub experience: u64,
}

#[derive(Debug)]
pub struct Inventory {
    pub items: Vec<String>,
    pub capacity: usize,
}

impl Inventory {
    pub fn new(capacity: usize) -> Self {
        Self {
            items: Vec::new(),
            capacity,
        }
    }

    pub fn add_item(&mut self, item: String) -> bool {
        if self.items.len() < self.capacity {
            self.items.push(item);
            true
        } else {
            false
        }
    }

    pub fn remove_item(&mut self, index: usize) -> Option<String> {
        if index < self.items.len() {
            Some(self.items.remove(index))
        } else {
            None
        }
    }
}

// Fixed: Removed Clone derive to avoid issues with &mut Inventory
// Option 1: Remove Clone if it's not needed
#[derive(Debug)]
pub struct UiData<'a> {
    pub player_stats: &'a Stats,
    pub player_pos: Vec3,
    pub inventory: &'a mut Inventory,
}

impl<'a> UiData<'a> {
    pub fn new(player_stats: &'a Stats, player_pos: Vec3, inventory: &'a mut Inventory) -> Self {
        Self {
            player_stats,
            player_pos,
            inventory,
        }
    }
}

// Alternative implementation using interior mutability if Clone is required
// This would be used instead of the above UiData struct
#[cfg(feature = "clone-ui-data")]
mod cloneable_ui_data {
    use super::*;
    use std::cell::RefCell;

    #[derive(Clone, Debug)]
    pub struct UiDataCloneable<'a> {
        pub player_stats: &'a Stats,
        pub player_pos: Vec3,
        pub inventory: &'a RefCell<Inventory>,
    }

    impl<'a> UiDataCloneable<'a> {
        pub fn new(
            player_stats: &'a Stats,
            player_pos: Vec3,
            inventory: &'a RefCell<Inventory>,
        ) -> Self {
            Self {
                player_stats,
                player_pos,
                inventory,
            }
        }

        // Helper method to access inventory mutably
        pub fn with_inventory_mut<F, R>(&self, f: F) -> R
        where
            F: FnOnce(&mut Inventory) -> R,
        {
            f(&mut self.inventory.borrow_mut())
        }
    }
}

#[cfg(feature = "clone-ui-data")]
pub use cloneable_ui_data::UiDataCloneable;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_stats_creation() {
        let stats = Stats {
            health: 100.0,
            mana: 50.0,
            level: 5,
            experience: 1000,
        };

        assert_eq!(stats.health, 100.0);
        assert_eq!(stats.mana, 50.0);
        assert_eq!(stats.level, 5);
        assert_eq!(stats.experience, 1000);
    }

    #[test]
    fn test_inventory_creation() {
        let inventory = Inventory::new(10);
        assert_eq!(inventory.capacity, 10);
        assert_eq!(inventory.items.len(), 0);
    }

    #[test]
    fn test_inventory_add_item() {
        let mut inventory = Inventory::new(2);
        assert!(inventory.add_item("sword".to_string()));
        assert!(inventory.add_item("shield".to_string()));
        assert!(!inventory.add_item("potion".to_string())); // Should fail, capacity reached
        assert_eq!(inventory.items.len(), 2);
    }

    #[test]
    fn test_inventory_remove_item() {
        let mut inventory = Inventory::new(5);
        inventory.add_item("sword".to_string());
        inventory.add_item("shield".to_string());

        let removed = inventory.remove_item(0);
        assert_eq!(removed, Some("sword".to_string()));
        assert_eq!(inventory.items.len(), 1);

        let invalid_remove = inventory.remove_item(10);
        assert_eq!(invalid_remove, None);
    }

    #[test]
    fn test_ui_data_creation() {
        let stats = Stats {
            health: 100.0,
            mana: 50.0,
            level: 1,
            experience: 0,
        };

        let mut inventory = Inventory::new(10);
        let pos = glam::Vec3::new(0.0, 0.0, 0.0);

        let ui_data = UiData::new(&stats, pos, &mut inventory);
        assert_eq!(ui_data.player_pos, pos);
        assert_eq!(ui_data.player_stats.level, 1);
    }

    #[cfg(feature = "clone-ui-data")]
    #[test]
    fn test_cloneable_ui_data() {
        use std::cell::RefCell;

        let stats = Stats {
            health: 100.0,
            mana: 50.0,
            level: 1,
            experience: 0,
        };

        let inventory = RefCell::new(Inventory::new(10));
        let pos = glam::Vec3::new(1.0, 2.0, 3.0);

        let ui_data = UiDataCloneable::new(&stats, pos, &inventory);
        let cloned = ui_data.clone();

        assert_eq!(cloned.player_pos, pos);
        assert_eq!(cloned.player_stats.level, 1);

        // Test mutable access
        ui_data.with_inventory_mut(|inv| {
            inv.add_item("test_item".to_string());
        });

        // Verify the item was added
        let borrowed = inventory.borrow();
        assert_eq!(borrowed.items.len(), 1);
        assert_eq!(borrowed.items[0], "test_item");
    }
}
